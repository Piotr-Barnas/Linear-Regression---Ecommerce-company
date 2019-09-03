# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:57:29 2019

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ecom = pd.read_csv('Ecommerce Customers')
print(ecom.head())
ecom.info()
print(ecom.describe())


sns.set_style(style='whitegrid')

sns.jointplot(x = 'Time on Website', y = 'Yearly Amount Spent', data = ecom)
sns.jointplot(x = 'Time on App', y = 'Yearly Amount Spent', data = ecom)
sns.jointplot(x = 'Time on App', y = 'Yearly Amount Spent', data = ecom, kind="hex")
sns.pairplot(data=ecom)
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=ecom)
plt.figure()

########################################################################

#print(ecom.columns)
X=ecom[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]
y=ecom['Yearly Amount Spent']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression 
lm = LinearRegression()

print(lm.fit(X_train, y_train))
print(lm.coef_)

predictions = lm.predict(X_test)


sns.scatterplot(y_test, predictions)
plt.figure()

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.distplot(y_test-predictions)

coef = pd.DataFrame(data=lm.coef_, index=['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership'], columns=['Coeffecient'])
print(coef)