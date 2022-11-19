# Port Scanning Detection with Machine Learning (User Manual)

## Table Of Contents

- [Port Scanning Detection with Machine Learning](#port-scanning-detection-with-machine-learning-user-manual)
  * [Table Of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Requirements](#requirements)
    + [Executing PreProcessing.ipynb](#executing-preprocessingipynb)
    + [Executing Training.ipynb](#executing-trainingipynb)
    + [Executing Testing.ipynb](#executing-testingipynb)
  * [Authors](#authors)

## Getting Started

### Requirements

- Copy the `dataset` folder and `models` folder to the root folder (MyDrive) of your Google Drive.

- Google CoLab is required to access each .ipynb file.
    - To import, click on `File -> Open Notebook`.

### Executing PreProcessing.ipynb

-  This file will do the following:
    1. Fix the columns in the raw datasets from Group 11, Group 12, and Group 16.
    2. Label data for each individual dataset.
    3. Combine all datasets into one.
    4. Clean the combined dataset, and save it as `all_data.csv` in the `dataset` folder. This file is already present inside the `dataset` folder, so running this will replace it.  

- Click on `Runtime -> Run All` to execute everything at once. 

### Executing Training.ipynb

-  This file will do the following:
    1. Import  `all_data.csv` generated in PreProcessing.ipynb. 
    2. Transform the dataset such that 30% of data is labelled as 1 (attack), and 70% of data is labelled as 0 (beneign).
    3. Execute all eight algorithms, with a confusion matrix shown for each algorithm.
    4. Plot graphs for accuracy, recall, precision, processing time, and all of the above.
    5. Export all models to the `models` folder. There are already existing models in the `models` folder, so running this will replace them.

- Click on `Runtime -> Run All` to execute everything at once. 

### Executing Testing.ipynb

- This uses an alternative dataset for preprocessing and training.

- Everything mentioned previously be will be performed by this file, except that it will now import the models exported by `Training.ipynb`, and will not transform the dataset to make it 30% attack traffic and 70% beneign traffic.

- Click on `Runtime -> Run All` to execute everything at once.  

## Authors

- Tay Wei Jie

- Ng Wei Liang

- Koh Cheng Kiat

- Lum Zheng Jie

- Low Wai Qun

- Quah Kian Yang

 
