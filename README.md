# information-sec-project

This project is a prototype of a solution of problem submitted in accordance with **Project**  as part of completing course CA-724 Information Security. 

## Problem  
Train and test a model to classify fraddulent and non-fraduelnt calls. 


## How to Run  
Make sure you have python Installed. 
In terminal , run the following  
```
pip install -r requirements.txt
```

To download the original dataset  
```
python src/dataset_download.py
python src/preprocess.py
```
This sets up the preprocessed data.

To Train

```
python src/conversion/preprocess.py
python src/conversion/train.py
```

Results be stored on results directory, Results can be verified using either Variational Autoencoder, or Gaussian Mixture Models.


