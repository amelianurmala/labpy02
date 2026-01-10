import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score, confusion_matrix
from imblearn.over_sampling import RandomOverSampler

df = pd.read_csv('loan_data.csv')

df = df.dropna()

le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

X = df.drop('Loan_Status', axis=1)
Y = df['Loan_Status']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=10
)

ros = RandomOverSampler()
X_train, Y_train = ros.fit_resample(X_train, Y_train)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(kernel='rbf')
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

print("ROC AUC Score:", roc_auc_score(Y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))
