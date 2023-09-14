## Breast Cancer Classification using Support Vector Machine (SVM)

This repository contains a Python script that demonstrates the use of Support Vector Machine (SVM) for classifying breast cancer data from the Scikit-Learn library. SVMs are well-suited for the classification of complex datasets like the breast cancer dataset provided in Scikit-Learn's datasets module.
Prerequisites

Before running the code, make sure you have the following Python libraries installed:

    Scikit-Learn (sklearn)
    NumPy (numpy)

You can install these libraries using pip:

    pip install scikit-learn numpy

# Usage

  Clone the repository or download the script.

  Run the script using a Python interpreter:

    python breast_cancer_classification.py

# Code Explanation
   The script begins by importing the necessary libraries, including Scikit-Learn and its datasets module.
   
  The breast cancer dataset is loaded from Scikit-Learn's datasets module. This dataset contains features related to breast cancer biopsies and binary labels indicating whether the tumors are malignant or benign.
    
  The dataset is split into training and testing sets using the train_test_split function from Scikit-Learn.
    
  A Support Vector Machine (SVM) classifier with a linear kernel and a regularization parameter (C) set to 1 is initialized.
    
  The classifier is trained on the training data using the fit method.
  
  Predictions are made on the test data using the predict method.
  
  The accuracy of the SVM classifier is computed using Scikit-Learn's accuracy_score function from the metrics module.
  
  The accuracy score is printed to the console, indicating how well the SVM classifier performs on the test data.
  
  Optionally, you can uncomment the loop to print the actual and predicted class labels for the first ten samples in the test set.

# Results
The script prints the accuracy of the SVM classifier, indicating its performance in classifying breast cancer data.

Accuracy of the model averages around 95%

Feel free to modify and extend this code for your own experiments or use cases.
