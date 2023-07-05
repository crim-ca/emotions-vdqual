# VDQUAL-Émotions  <!-- omit in toc -->
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][license-file]
> Le contenu suivant est également [disponible en anglais](README_EN.md).

## Table des matières <!-- omit in toc -->
- [Licence](#licence)
- [Introduction](#introduction)
- [Utilisation de Span-Aste](#utilisation-de-span-aste)
- [Données annotées pour la détection d'émotions en français](#données-annotées-pour-la-détection-démotions-en-français)
- [Description des fichiers](#description-des-fichiers)
- [Contributeurs et remerciements](#contributeurs-et-remerciements)
- [Références](#références)
  - [Citation](#citation)

## Licence

Ce travail est sous licence [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[Licence CC BY-NC-SA 4.0][license-file] <br>
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[license-file]: ./LICENSE
Voir le fichier [LICENCE](LICENSE) pour plus de détails.

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/

[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

Veuillez voir également les requis de [Citation](#Citation).
<br><br>

## Introduction 
**VDQUAL-emotions.**

Ce code a été utilisé dans le cadre d'un projet avec le [FAR]((https://www.baf-far.ca/fr)) 
(Fonds pour l'accessibilité de la radiodiffusion).
Le projet global vise à développer un [outil VDQUAL](https://github.com/crim-ca/vdqual-outil) de vérification de la qualité des vidéodescriptions (VD) 
de films et séries télévisées en anglais ou en français.  Il est aussi disponible en ligne : https://vdqual.crim.ca/.
L'une des fonctionnalités de l'outil est la détection d'émotions dans des vidéodescriptions en français 
en distinguant les états émotifs des actions émotives. Les fichiers de ce répertoire concernent 
cette fonctionnalité.
<br><br>

## Utilisation de Span-Aste

Nous avons utilisé le code de [Span-Aste](https://github.com/chiayewken/Span-ASTE), initialement prévu pour de 
la triple extraction de sentiments d'empans de texte (aspect, expression de l'opinion et polarité du sentiment) 
pour faire la détection d'états émotifs ou d'actions émotives.

Les triplets ont été adaptés en conséquence : 
  - expression de l'opinion --> expression de l'émotion ;
  - aspect  --> source de l'émotion (personne qui ressent l'émotion) ;
  - polarité du sentiment --> modalité de l'émotion (état émotif ou action émotive).

  - Les données ont été annotées en suivant cette convention. Puis, nous avons entrainé un modèle sur ces données annotées.
Le modèle ainsi crée permet de faire des prédictions sur de nouvelles données.

Nous fournissons les données annotées en français (en deux formats : JSON et TXT) qui ont servi à l'entraînement et 
à l'évaluation de notre modèle. Nous fournissons aussi le modèle que nous avons entrainé sur ces données.

Nous vous référons au code de Span-Aste si vous vouliez réentrainer le modèle.
<br><br>
## Données annotées pour la détection d'émotions en français

Les données annotées sont en format JSON et en format TXT (ce dernier format est celui utilisé par Span-Aste).
Les phrases brutes proviennent du corpus [FrVD](https://github.com/crim-ca/FrVD). Le corpus original utilise
des vidéodescriptions transcrites dans le cadre de projets antérieurs financés par l'Office des personnes handicapées 
du Québec (OPHQ) et le Programme de soutien, à la valorisation et au transfert (PSVT). 

Ici, les vidéodescriptions ont été sélectionnées pour leur possible présence d'émotions. Les phrases ont été extraites 
du corpus et mélangées pour être présentées dans un ordre aléatoire qui ne tient pas compte de l'intégrité d'une oeuvre 
(afin de limiter le biais interprétatif par connaissance du contexte situationnel).
Chaque fichier JSON contient environ 250 vidéodescriptions (une phrase par ligne, 
mais une vidéodescription peut contenir plusieurs phrases).
Deux annotatrices se sont répartis l'annotation des fichiers. Un petit ensemble de fichiers a été annotés en double. 
L'accord inter-annotateur est le suivant : 
 - accord sur la détection d'une expression émotive (un chevauchement est considéré comme positif): f1 score de 0.829466
 - accord sur la modalité de l'émotion : Kappa de Cohen de 0.880149.
<br><br>

## Description des fichiers
Le répertoire contant données et modèle est disponible [ici](https://drive.google.com/drive/folders/1sLiYm2nzTi7_9cls_-Mn_CCwItdYTs3C). 
Il faut faire une demande d'accès pour accéder aux fichiers décrits ci-dessous.

1. Les fichiers sont annotés au format JSON. Ils sont disponibles dans le répertoire `data/gold_json.zip`
(à décompresser) et ont été répartis en trois répertoires (train, test et val).

2. Ils doivent être transformés en fichiers TXT pour être utilisés par Span-Aste. 
Le format attendu est un document avec une phrase par ligne : `sentence#### #### ####[triplet_0, ..., triplet_n]`.
Pour cela, nous avons utilisé le script `transform_json_to_txt.py`.

3. Les données transformées sont disponibles ici : `data/split_txt.zip`.

4.  Le modèle entrainé en utilisant le code de Span_aste est disponible ici : `model.tar.gz`.
<br><br>

## Contributeurs et remerciements

Le projet a reçu un financement du Fonds d'accessibilité à la radiodiffusion([FAR]((https://www.baf-far.ca/fr))).

Les données annotées proviennent d'une partie corpus [Fr-VD](https://github.com/crim-ca/FrVD). 

L'entraînement du modèle se fait grâce à l'article
[Learning Span-Level Interactions for Aspect Sentiment Triplet Extraction](https://aclanthology.org/2021.acl-long.367)
de Xu et al., ACL-IJCNLP 2021. Le code est disponible ici : https://github.com/chiayewken/Span-ASTE.
<br><br>

## Références

**VDQUAL-emotions : Jeu de données et modèle pour la détection d'émotions dans des vidéodescriptions en français.**

Veuillez référencer ces travaux et le jeu de données à l'aide de la citation suivante.
### Citation

```bibtex
@techreport{VDQUAL_tool,
    title = "Outil de vérification de la qualité des vidéodescriptions en français et en anglais.",
    author = "Edith Galy, Azur Handan",
    institution = "Centre de recherche informatique de Montréal (CRIM)",
    address = "405 Ogilvy Avenue #101, Montréal, QC H3N 1M3",
    year = 2023,
    month = jun
}
```
