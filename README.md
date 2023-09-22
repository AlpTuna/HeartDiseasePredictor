# Cardiology Decision Tree Classifier
This Python code represents a decision tree classifier for predicting the presence or absence of heart disease based on various patient attributes. It uses the scikit-learn library for machine learning and pandas for data manipulation.

## Table of Contents
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Dataset](#dataset)
* [Model Training](#dataset)
* [Visualization](#visualization)
* [Predictions](#predictions)

## Getting Started
Before using this code, make sure you have the necessary libraries installed. You can install them using pip:

``` bash
pip install pandas scikit-learn joblib
```
## Usage
The code consists of several components:

* **Loading or Training the Model**: The code checks if a pre-trained model ('**patientDataset.joblib**') exists. If not, it trains a new decision tree classifier on a provided dataset ('**heart.csv**') and saves it as '**patientDataset.joblib**'.

* **Predict**: The **Predict** function takes a list of patient attributes as input and predicts whether the patient has heart disease or not.
  
* **ExportDecisionTreeGraph**: This function exports the DecisionTree as a .dot file, which can be visualized to understand the algorithm's decision-making process.

## Dataset
The code assumes that a dataset named heart.csv is available for training. This dataset should contain the following columns:

* Age
* Resting BP
* Cholesterol
* Fasting Blood Sugar (Fasting BS)
* Maximum Heart Rate (MaxHR)
* Oldpeak
* Gender
* Chest Pain Type
* Resting ECG
* Exercise-Induced Angina (Exercise Angina)
* ST Segment Slope (ST Slope)
* Heart Disease (Target variable: 'No' for no heart disease, 'Yes' for heart disease)

## Model Training
If there is no pre-trained model, the code performs the following steps to train a new one:

* Preprocesses the dataset, including label encoding for categorical features.
* Splits the data into training and testing sets (typically 80% training, 20% testing).
* Trains a DecisionTreeClassifier on the training data.
* Calculates and prints the accuracy score on the test data.
* The trained model is then saved as patientDataset.joblib for future use.

## Visualization
The code uses '**tree.export_graphviz**' to export the decision tree as a .dot file **('cardiologyDecisionTree.dot')**. You can visualize this file using graph visualization software like Graphviz.

## Predictions
You can make predictions using the **Predict** function by providing a list of patient attributes as input. It will return '**Normal**' if the prediction is '**No**' (no heart disease) and '**Heart Disease**' if the prediction is '**Yes**' (heart disease).

Example:

```python
result = Predict([40, 140, 289, 0, 172, 0.0, 1, 1, 1, 0, 2])
print(result)  # Output: 'Heart Disease'
```
