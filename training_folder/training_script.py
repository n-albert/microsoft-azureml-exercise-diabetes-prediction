from azureml.core import Run
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Get the experiment run context
run = Run.get_context()

# Prepare the dataset
diabetes = pd.read_csv('data.csv')

# Nikita Albert's Note: Patient ID should not be a part of the training loop, 
# since we do not want an ID number to influence a model's decisioning
# as to whether the given entry has diabetes or not.
# I am including it because the exercise did not call for its removal.
X, y = diabetes[['PatientID', 'Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness', 'SerumInsulin', 'BMI', 'DiabetesPedigree', 'Age']].values, diabetes['Diabetic'].values
X_train_data, X_test_data, y_train_labels, y_test_labels = train_test_split(X, y, test_size=0.30)

# Train a logistic regression model
reg = 0.1
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train_data, y_train_labels)

# calculate accuracy
y_predicted_labels = model.predict(X_test_data)
acc = np.average(y_predicted_labels == y_test_labels)
run.log('Accuracy', np.float(acc))

# Save the trained model
os.makedirs('outputs', exist_ok=True)
joblib.dump(value=model, filename='outputs/model.pkl')

run.complete()