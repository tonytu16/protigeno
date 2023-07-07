# ProtiGeno

This repository contains code for "ProtiGeno: a prokaryotic short gene finder using protein language models" Tony Tu, Gautham Krishna Sankar Ramalaxmi
, Amirali Aghazadeh to appear at ICML WCB 2023. 

### Abstract
<a id=abstract></a>
Prokaryotic gene prediction plays an important role in understanding the biology of organisms and their function with applications in medicine and biotechnology. Although the current gene finders are highly sensitive in finding long genes, their sensitivity decreases noticeably in finding shorter genes (<180 nts). The culprit is the lack of short annotated gene data to allow learning distinguishing features in short open reading frames (ORFs). We develop a deep learningbased method called ProtiGeno, specifically targeting short prokaryotic genes using a protein language model trained on millions of evolved proteins. In systematic large-scale experiments on 4288 prokaryotic genomes, we demonstrate that ProtiGeno predicts short coding and noncoding genes with significantly higher accuracy and recall than the current state-of-the-art gene finders. We discuss the predictive features of ProtiGeno and possible limitations by visualizing the three dimensional structure of the predicted short genes.

### Quick Start
All codes are uploaded in the ipython notebook file

Run each cell in order. Alternatively, hold shift and enter to run all cells. Because ProtiGeno uses ESM-1b protein language models to calculate sequence embeddings, each genome could take a few seconds or up to a minute to run depending on the number of sequences and the lengths of the sequences available. Feel free to open a github issue if you run into problems! 

### ProtiGeno genome-wise performance evaluation

All csv files for protigeno + baseline evaluation results are uploaded under /results folder, which contains detailed genome-specific accuracy, precision, recall and F-1 score, in the following table, we report the percentage of genomes on which protigeno outperforms the baseline methods. Note that the percentages are calculated based on 4280 genomes instead of 4288. Since after filtering duplicates, 8 genomes either do not have any coding regions or non-coding regions. We exclude these 8 genomes and only include genomes which have both coding regions and noncoding regions. 

| Baseline Methods | % of genomes protigeno outperforms (Accuracy) | % of genomes protigeno outperforms (Precision) | % of genomes protigeno outperforms (Recall) | % of genomes protigeno outperforms (F1) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| GeneMarkS (GP) | 73.9 | 37.7 | 88.5 | 74.1 |
| GeneMarkS (PGP)  | 80.2 | 37.7 | 91.4 | 80.5 |
| Prodigal (GP)  | 87.9 | 37.8 | 96.1 | 88.2 | 
| Prodigal (PGP)  | 91.6 | 37.9 | 97.4 | 92.0 | 
| FragGeneScan (GP)  | 91.5 | 37.9 | 99.3 | 98.2 |
| FragGeneScan (PGP)  | 93.5 | 37.9 | 99.5 | 98.9 |

### Runtime Information

Our method consists of two components: 1). Bulk computing sequence embeddings using protein language model, 2). Training binary classifier using the obtained embeddings. We used code from FLIP - Bio Benchmarks for Protein Engineering (github link: [https://github.com/facebookresearch/esm/tree/main/esm](https://github.com/J-SNACKKB/FLIP/blob/main/baselines/embeddings/embeddings.py)) for bulk computing sequence embeddings. The protein language model we used in the paper (ESM-1b) can be downloaded from facebook esm (github link: https://github.com/facebookresearch/esm/tree/main). All runtime information for coding regions embeddings bulk computation can be found in the coding_regions_runtime folder and all runtime information for noncoding regions embeddings bulk computation can be found in the noncoding_regions_runtime folder. A complete runtime overview can be found in runtime.csv file. All sequences are processed using NVIDIA RTX A6000 GPU. 

For the second component -- binary classifier, all parameters used for training binary classifiers are included in appendix E in the original paper. The binary classifiers are trained on 2.3 GHz 8-Core Intel Core i9 and each takes about an hour to train. 






Please feel free to reach out to us if you have any questions!
