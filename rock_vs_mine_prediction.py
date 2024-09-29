# -*- coding: utf-8 -*-
"""Rock Vs Mine Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gZ7Jtf4tBgfNWqi61SImqSU21f11Y066
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Data Processing"""

#loading a dataset to a pandas Dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header=None)

sonar_data.head()

# no of rows and columns
sonar_data.shape

#describe --> statistical measures of the data
sonar_data.describe()

sonar_data[60].value_counts()



"""M --> Mines
R --> Rocks
"""

sonar_data.groupby(60).mean()

# separating data and labels
x = sonar_data.drop(columns=60, axis=1)
y = sonar_data[60]

print(x)
print(y)



"""Training and Test data

"""

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.1, stratify=y, random_state=1)

print(x.shape, X_train.shape, X_test.shape)



"""Model Training --> Logistic Regression"""

model = LogisticRegression()

# training the logistic Regression model with training data
model.fit(X_train, Y_train)

print(X_train)
print(Y_train)



"""Model Evaluation"""

from re import X
#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)



"""Making a Predective System"""

input_data = (0.0187,0.0346,0.0168,0.0177,0.0393,0.1630,0.2028,0.1694,0.2328,0.2684,0.3108,0.2933,0.2275,0.0994,0.1801,0.2200,0.2732,0.2862,0.2034,0.1740,0.4130,0.6879,0.8120,0.8453,0.8919,0.9300,0.9987,1.0000,0.8104,0.6199,0.6041,0.5547,0.4160,0.1472,0.0849,0.0608,0.0969,0.1411,0.1676,0.1200,0.1201,0.1036,0.1977,0.1339,0.0902,0.1085,0.1521,0.1363,0.0858,0.0290,0.0203,0.0116,0.0098,0.0199,0.0033,0.0101,0.0065,0.0115,0.0193,0.0157)

#changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a mine')

