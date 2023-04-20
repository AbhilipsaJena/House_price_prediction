# -*- coding: utf-8 -*-
"""House price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D9NhOVaTtbEImUsynR5K_cI3SXqPZ7VA
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

from sklearn.datasets import fetch_california_housing

california_dataset = fetch_california_housing()

print(california_dataset)

#load california dataset to pandas
california_dataframe = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)

# Add target variable to DataFrame
# target=price
california_dataframe['target'] = california_dataset.target

print(california_dataframe.head())

california_dataframe.shape

california_dataframe.isnull().sum()

california_dataframe.describe()

correlation = california_dataframe.corr()

# build a heatmap for the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

#split train and test
X=california_dataframe.drop(['target'],axis=1)

Y=california_dataframe['target']

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

# loading the model
model = XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train)

training_data_prediction = model.predict(X_train)

print(training_data_prediction)

# R squared error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Predicted Price")
plt.show()

test_data_prediction = model.predict(X_test)

# R squared error
score_1 = metrics.r2_score(Y_test, test_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)