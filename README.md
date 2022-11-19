# Port Scanning Detection with Machine Learning (User Manual)

## Table Of Contents

- [Port Scanning Detection with Machine Learning (User Manual)](#port-scanning-detection-with-machine-learning-user-manual)
  - [Table Of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Executing PreProcessing.ipynb](#executing-preprocessingipynb)
    - [Executing Training.ipynb](#executing-trainingipynb)
    - [Executing Testing.ipynb](#executing-testingipynb)
    - [Generating alternate dataset](#generating-alternate-dataset)
    - [Dashboard](#dashboard)
  - [Authors](#authors)

## Getting Started

### Requirements

- Copy all three .ipynb files, the `dataset` folder and `models` folder to the root folder (MyDrive) of your Google Drive.

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

- This uses an alternative dataset, `testing_data.csv`, for preprocessing and training.

- Everything mentioned previously be will be performed by this file, except that it will now import the models exported by `Training.ipynb`, and will not transform the dataset to make it 30% attack traffic and 70% beneign traffic.

- Click on `Runtime -> Run All` to execute everything at once.  

### Generating alternate dataset

- This requires `docker` and `docker-compose`
- To generate the alternate dataset, do the following:
    1. Navigate to the `alternate_dataset_environment` folder
    2. Run `docker-compose up -d --scale client=50`
    3. Run `docker-compose exec server /bin/services.sh` to start the services on the server
    4. Run `docker-compose exec kali nmap server`
    5. Browse kibana via `http://localhost:5601`
    6. Click on Discovery and filter `event.dataset: "flow"`
    7. Click on `Share > CSV Reports > Generate CSV` and download the csv

### Dashboard

- Click on `dashboard-original.html` (based on the original dataset for training) or `dashboard-alternate.html` (based on the alternate dataset for testing) in the `dashboard` folder to view the graphs for the following:
    1. Accuracy
    2. Precision
    3. Recall
    4. Processing Time
    5. All of the above


## Authors

- Tay Wei Jie

- Ng Wei Liang

- Koh Cheng Kiat

- Lum Zheng Jie

- Low Wai Qun

- Quah Kian Yang

 
