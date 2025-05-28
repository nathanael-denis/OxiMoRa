OxiMoRa: Monitoring corrosion using harmonic radar signals

This repository contains the code, resources, and workflows used to train and analyze machine learning models for detecting corrosion using harmonic radar technology. The project focuses on leveraging raw IQ signals, advanced data processing, and deep learning techniques to monitor corrosion, including scenarios involving rust-induced harmonic emissions.

Repository structure:

----
Directories
----

images/ (Empty) Contains the images generated from IQ sample files for use in machine learning tasks. These images encapsulate the information needed for training, validation, and testing models. The images generated from iqToRichImages will be saved here.

rawIQ/ Contains the raw IQ sample files, which are the foundational input data for the project. These signals are processed into meaningful features for the machine learning pipeline.
IQ files are heavy and not provided in this repository; they must be fetched https://figshare.com/s/8f0fa4bc6f1d883cdf0a and https://figshare.com/s/16415cff18b5663eae1c

results/ has the metrics for each individual round of each experiments, compiling all experimental data

output/ has a collection of images that are already generated and sorted, so that they can be used to test the whole classification pipeline (training + testing). The images are derived from IQ samples collected in the third setup --- Pipeline internal oxides. If you run either splitUnbalanced.py or splitBalanced.py, the images will be sent there, so it is better to clean this directory before this to avoid conflicts.

----
Python scripts
----

trainingLocal.py The main training script for local environments. Implements the model training loop, utilizing harmonic radar data processed into rich images.

distributedTrainingLocal.py Facilitates distributed training for leveraging multi-GPU setups or HPC clusters. Ideal for scaling the model training on large datasets or experimenting with enhanced architectures.

iqToRichImages.py Processes raw IQ sample files into rich grayscale images. This critical preprocessing step converts raw signal data into an image representation suitable for deep learning.

splitBalanced.py Splits datasets into balanced training, validation, and test sets. Ensures that the class distribution is consistent across splits to improve training performance.

splitUnbalanced.py Alternative dataset splitting script, designed for cases where class imbalances are not adjusted. Useful for analyzing real-world distributions.

confusion_matrix.py and confusion_matrix2.py generate the confusion matrixes for the article.

----
GNU Workflow
----

harmonic_radar.grc contain the graphical representation of signal processing flowgraphs, which GRC translates into Python scripts for execution.
It can be used directly in GNU Radio Companion to collect data using f0=2.5GHz as a fundamental frequency (tunable). We use a USRP X310 and a HackRF for 
the experiments, hence the UHD: USRP Source (RX) and Osmocom Sink (TX)


Getting Started
----
1) Clone the repository
2) Prepare the datasets: Place your IQ sample files in the rawIQ/ directory and run iqToRichImages.py to generate rich images.
3) Split the datasets into training, validation, and test sets using splitBalanced.py or splitUnbalanced.py.
4) Train the model using trainingLocal.py or distributedTrainingLocal.py. On a laptop, use trainingLocal.py

----

Methodology

----

This provides the full methodology; the code in this repository is associated with the workstation steps in the diagram.

![image](https://github.com/user-attachments/assets/992ae748-7f48-4c21-8a7f-3c130c2e3b85)


