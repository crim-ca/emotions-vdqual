"""
Script that parses a JSON file that contains annotations of triplet (emotion expression, target and modality of emotion)
 with the purpose of creating the input files that Span-ASTE needs to train a new model
 or to make predictions with a pre-trained model
The format of these files is one sentence per line (with an empty list for triplets to make
predictions, as specified in https://github.com/chiayewken/Span-ASTE#data-format)

There is two modes of operation:
- TRAIN_MODE = True: The script will parse all the JSON files in the folder specified in the config file
and outputs one TXT file par split (train, tst, val)
- TRAIN_MODE = False: The script will parse all the JSON files in the folder specified in the config file
and outputs one TXT file per JSON file. This is useful to make predictions with a pre-trained model.
"""

import os
import json
from configparser import ConfigParser

# Read values in config file
config = ConfigParser()
config.read("config.ini")
GOLD_FOLDER_PATH = config["span_aste"]["gold_folder_path"]
TRAIN_MODE = config.getboolean("span_aste", "train_mode")

# Output will be a single TXT file that corresponds to a dataset split (trn, val, tst)
if TRAIN_MODE:
    out_lines = []
    for file in os.listdir(GOLD_FOLDER_PATH):
        if file.endswith(".json"):
            GOLD_FILE_PATH = os.path.join(GOLD_FOLDER_PATH, file)
            with open(GOLD_FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

                for sentence in data:
                    triplets = []
                    text = sentence["text"].strip().replace("\n", " ")

                    for annotation in sentence["annotations"]:
                        # Original triplet format: (aspect target, opinion expression and sentiment polarity)
                        # Refer to this link for further information: https://github.com/chiayewken/Span-ASTE
                        # Format for our purposes: (target tokens, emotion tokens, modality)
                        triple = [[], [], ""]
                        for target in annotation["target"]:
                            triple[0].extend(target["indices"]["token"])
                        triple[1].extend(annotation["emotion"]["indices"]["token"])
                        # Map modality to valid polarity values
                        modality = ""
                        if annotation["modality"] == "state":
                            modality = "POS"
                        else:
                            modality = "NEG"
                        triple[2] = modality

                        if triple[0] and triple[1] and modality:
                            triple[0].sort()
                            triple[1].sort()
                            triplets.append(tuple(triple))

                    if triplets:
                        out_lines.append(text + "#### #### ####" + str(triplets))

                    # In order to train a new Span-ASTE model, the training dataset should consist of sentences
                    # with a corresponding triplet annotation. A sentence without a triplet (a negative example)
                    # causes the training code to fail. As such, here we will append a "dummy" triplet annotation
                    # (https://github.com/chiayewken/Span-ASTE/blob/7cbf03569e25829113fbc245a97184dde154d42c/aste/data_utils.py#L58)
                    # to sentences with no associated triplets
                    else:
                        out_lines.append(text + "#### #### ####[([0], [0], 'NEU')]")

    # Write output TXT file
    SPLIT_FILE_PATH = config["span_aste"]["split_file_path"]
    with open(SPLIT_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print("Output JSON file with %d lines saved to \"%s\"" % (len(out_lines), SPLIT_FILE_PATH))


# Output will be one TXT file per input JSON file
# These output files can then be used to make predictions using a pre-traind Span-ASTE model
else:
    for file in os.listdir(GOLD_FOLDER_PATH):
        if file.endswith(".json"):
            # Path to the folder that will contain the output pre-formatted files
            TEMP_FOLDER_PATH = config["span_aste"]["temp_folder_path"]

            # For each JSON file we find in our input folder
            # We will create a text file with the same name but with a TXT extension
            GOLD_FILE_PATH = os.path.join(GOLD_FOLDER_PATH, file)
            TEMP_FILE_PATH = os.path.join(TEMP_FOLDER_PATH, os.path.splitext(file)[0] + '.txt')

            # Retrieve text of sentences
            list_sentences = []
            with open(GOLD_FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                for sentence in data:
                    text = sentence["text"].strip()
                    # Some phrases in the XML files retrieved from Inception contain newline characters
                    # We replace these with whitespaces so the text files we will output in this script
                    # contain exactly one phrase per line
                    text = text.replace("\n", " ")
                    # Add the empty list of triplets that Span-ASTE requires to make predictions
                    list_sentences.append(text + "#### #### ####[]")

            with open(TEMP_FILE_PATH, "w", encoding="utf-8") as f:
                f.write("\n".join(list_sentences))
