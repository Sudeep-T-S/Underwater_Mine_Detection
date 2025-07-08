import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

sonar_data = pd.read_csv('sonar.csv', header=None)

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_accuracy = accuracy_score(train_pred, Y_train)
test_accuracy = accuracy_score(test_pred, Y_test)

print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

filename = 'finalized_model_LR.sav'
pickle.dump(model, open(filename, 'wb'))