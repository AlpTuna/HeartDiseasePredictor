import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os


def ExportDecisionTreeGraph(): # Exports the DecisionTree as a .dot file (visualization of the algorithm)
    tree.export_graphviz(model,out_file = 'cardiologyDecisionTree.dot',
                        feature_names = ['Age','Resting BP','Cholestrol','Fasting BS','MaxHR','Oldpeak','Gender',
                                            'Chest Pain Type','Resting ECG','Exercise Angina','ST Slope'],
                        class_names = ['No','Yes'], label ='all', rounded = True, filled = True)


if os.path.isfile('patientDataset.joblib'):
    #If there is already a trained model
    model = joblib.load('patientDataset.joblib')
else:
    # If there is no trained model already, a new will be created and saved
    df = pd.read_csv('heart.csv')

    inputs = df.drop(['HeartDisease'],axis = 'columns')
    target = df['HeartDisease']

    inputs['Gender_n'] = LabelEncoder().fit_transform(inputs['Sex'])
    inputs['ChestPainType_n'] = LabelEncoder().fit_transform(inputs['ChestPainType'])
    inputs['RestingECG_n'] = LabelEncoder().fit_transform(inputs['RestingECG'])
    inputs['ExerciseAngina_n'] = LabelEncoder().fit_transform(inputs['ExerciseAngina'])
    inputs['ST_Slope_n'] = LabelEncoder().fit_transform(inputs['ST_Slope'])

    inputs_n = inputs.drop(columns = ['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope'])

    inputs_train,inputs_test,target_train,target_test = train_test_split(inputs_n,target,test_size = 0.20) 
    # This split usually gives around 80% percent accuracy score

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_train,target_train)
    joblib.dump(model,'patientDataset.joblib') # Saves the dataset

    predictions = model.predict(inputs_test)
    print('Accuracy Score:',accuracy_score(target_test,predictions))

    ExportDecisionTreeGraph()

# Encodings for inputs_n

# Gender: {Female : 0, Male : 1}
# ChestPainType: {ASY: 0, ATA : 1, NAP : 2,TA:3}
# RestingECG: {LVH: 0, Normal : 1, ST : 2}
# ExerciseAngina: {No: 0, Yes : 1}
# ST_Slope: {Down: 0, Flat : 1, Up: 2}


def Predict(attributes):
    x = model.predict([attributes])
    if x == [0]:
        return 'Normal'
    elif x == [1]:
        return 'Heart Disease'

Predict([40,140,289,0,172,0.0,1,1,1,0,2])