# Deep Learning Model Training on TinyImagenet-200

## Overview
This project is designed for training a deep learning model on a dataset using PyTorch in a JupyterNotebook script. The script includes functionalities for data loading, model training, and evaluation. The trained model's performance and training history are saved, and visualizations are generated.

## Getting Started


## Usage
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/sjc042/tiny-imagenet.git
    cd tiny-imagenet
    ```
2. **Downloading the dataset:**

    To use this code you will first need to download the dataset from
    it's website: http://cs231n.stanford.edu/tiny-imagenet-200.zip

    Alternatively, you can run the following command in your terminal
    if you have `wget` installed to download it to your current directory:
    ```
    wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
    ```
3. **Reorganize diretory:**

    - 2.1 
        Move tiny-imagenet-200.zip to 'data' directory
    - 2.2
        Inside /data/, unzip file:
        ```bash
        unzip tiny-imagenet-200.zip
        ```
    - 2.2
        Reorganize the directory structure by running:
        ```bash
        python ../tools/tinyimagenet_reorg.py
        ```
4. **Create Conda Environment:**
    ```bash
    conda create --name tinyimagenet python=3.8
    ```

5. **Check Environment:**
    ```bash
    conda list
    ```

6. **Activate the Environment:**
    ```bash
    conda activate tinyimagenet
    ```
    To deactivate, run:
    ```bash
    conda deactivate
    ```

7. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
