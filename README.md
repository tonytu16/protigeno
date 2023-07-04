# ProtiGeno

This repository contains code for "ProtiGeno: a prokaryotic short gene finder using protein language models" Tony Tu, Gautham Krishna Sankar Ramalaxmi
, Amirali Aghazadeh to appear at ICML WCB 2023. 

### Abstract
<a id=abstract></a>
Prokaryotic gene prediction plays an important role in understanding the biology of organisms and their function with applications in medicine and biotechnology. Although the current gene finders are highly sensitive in finding long genes, their sensitivity decreases noticeably in finding shorter genes (<180 nts). The culprit is the lack of short annotated gene data to allow learning distinguishing features in short open reading frames (ORFs). We develop a deep learningbased method called ProtiGeno, specifically targeting short prokaryotic genes using a protein language model trained on millions of evolved proteins. In systematic large-scale experiments on 4288 prokaryotic genomes, we demonstrate that ProtiGeno predicts short coding and noncoding genes with significantly higher accuracy and recall than the current state-of-the-art gene finders. We discuss the predictive features of ProtiGeno and possible limitations by visualizing the three dimensional structure of the predicted short genes.

### Quick Start
All codes are uploaded in the ipython notebook file

Run each cell in order. Alternatively, hold shift and enter to run all cells. Because ProtiGeno uses ESM-1b protein language models to calculate sequence embeddings, each genome could take a few seconds or up to a minute to run depending on the number of sequences and the lengths of the sequences available. Feel free to open a github issue if you run into problems! 

We have included the runtime information in this repo as well as results in the results folder. Please feel free to reach out to us if you have any questions!


