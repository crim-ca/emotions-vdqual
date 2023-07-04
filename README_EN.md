# VDQUAL-Emotions dataset <!-- omit in toc -->
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][license-file]
> The following content is also [available in french](README.md).
## Table of Contents <!-- omit in toc -->
- [License](#license)
- [Introduction](#introduction)
- [Using Span-Aste](#using-span-aste)
- [Annotated data for emotion detection in french](#annotated-data-for-emotion-detection-in-french)
- [Description of files](#description-of-files)
- [Contributors and Acknowledgments](#contributors-and-acknowledgments)
- [References](#references)
  - [Citation](#citation)

***

## License

This work is under the 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa] license for the french model and data used for emotion detection.

[CC BY-NC-SA 4.0 License][license-file] <br>
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[license-file]: ./LICENSE
See the [LICENSE](LICENSE) file for more details.

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/

[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

See also the [Citation](#Citation) requirements.
<br><br>
***

## Introduction

**VDQUAL-emotions.**

This code was used as part of a project with the [FAR]((https://www.baf-far.ca/en)) (Broadcasting Accessibility Fund).
The overall project aims to develop a [VDQUAL tool](https://github.com/crim-ca/vdqual-outil) for verifying the quality of video descriptions (VD)
films and television series in English or French. It's also available online [here](https://vdqual.crim.ca/).
One of the features of the tool is the detection of emotions in French video descriptions
distinguishing emotional states from emotional actions. The files in this directory  concern
this feature.
<br><br>
***

## Using Span-Aste

We used code from [Span-Aste](https://github.com/chiayewken/Span-ASTE), originally intended for triple span 
sentiment extraction of text (aspect, expression of opinion and polarity of feeling) to detect emotional states or
emotional actions.

The triplets have been adapted accordingly:
   - expression of opinion --> expression of emotion,
   - aspect --> source of the emotion (person who feels the emotion)
   - polarity of the feeling --> modality of the emotion (emotional state or emotional action).
The data was annotated following this convention. Then we trained a model on this annotated data.
The model thus created makes it possible to make predictions on new data.

We provide french annotated data (in two formats: JSON and TXT) that was used for training and evaluation
of our model. We also provide the model we trained on this data.

The directory containing the data and the model is available at:
We refer you to the Span-Aste code if you want to retrain the model.
<br><br>
***

## Annotated data for emotion detection in french

The annotated data is in JSON format and in TXT format (the latter format is the one used by Span-Aste).
The raw sentences come from the corpus [FrVD](https://github.com/crim-ca/FrVD). The original corpus uses
video descriptions transcribed as part of previous projects funded by the Office for Disabled People
du Québec (OPHQ) and the Support, Development and Transfer Program (PSVT).

Here, the video descriptions have been selected for their possible presence of emotions. Sentences were extracted
of the corpus and shuffled to be presented in a random order that does not take into account the integrity of a work
(in order to limit the interpretative bias through knowledge of the situational context).
Each file contains approximately 250 video descriptions (one sentence per line,
but a video description can contain several sentences).
Two annotators shared the annotation of the files. A small set of files was annotated twice.
The inter-annotator agreement is as follows:
  - agreement on the detection of an emotive expression (an overlap is considered positive): f1 score of 0.829466
  - agreement on the modality of the emotion: Cohen's Kappa of 0.880149.
<br><br>
***

## Description of files
The directory with data and template is available [here]
(https://drive.google.com/drive/folders/16y-YCS2aLRZ5Dg9zIs3mRCPsmQYOvWml).
An access request must be made to access the files described below.

1. Files are annotated in JSON format. They are available at the following address in the file 
`data/gold_json.zip` and have been distributed in three directory (train, test and val).

2. They must be transformed into TXT files to be used by Span-Aste.
The expected format is a document with one sentence per line: `sentence#### #### ####[triplet_0, ..., triplet_n]`.
For this, we used the `transform_json_to_txt.py` script.

3. The transformed data is available here: `data/split_txt.zip`.


4. The model trained using the code from Span_aste is available here: `model.tar.gz`.
<br><br>
***

## Contributors and Acknowledgments


The project received funding from the Broadcasting Accessibility Fund([FAR]((https://www.baf-far.ca/fr))).

The annotated data comes from a corpus part [Fr-VD](https://github.com/crim-ca/FrVD).

The training of the model is done thanks to the article
[Learning Span-Level Interactions for Aspect Sentiment Triplet Extraction](https://aclanthology.org/2021.acl-long.367)
from Xu et al., ACL-IJCNLP 2021. The code is available here: https://github.com/chiayewken/Span-ASTE.
<br><br>
***

## References

**VD-QUAL-emotions: Dataset and model for the detection of emotions in video descriptions in French.**

Please reference these works and the dataset using the following citation.

### Citation

```bibtex
@techreport{VDQUAL_Dataset,
   title = "VD-QUAL-emotions: Dataset and model for the detection of emotions in video descriptions in French.",
   author = "Edith Galy, Azur Handan",
   institution = "Computer Research Center of Montreal (CRIM)",
   address = "405 Ogilvy Avenue #101, Montreal, QC H3N 1M3",
   year = 2023,
   month = june
}
```