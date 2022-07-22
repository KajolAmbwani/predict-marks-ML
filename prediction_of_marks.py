# -*- coding: utf-8 -*-
"""prediction of marks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OiQbwrTGoj11RfSv4Qr6MBSxtcseb4YN
"""

# Commented out IPython magic to ensure Python compatibility.
#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#load data
url= "https://raw.githubusercontent.com/KajolAmbwani/predict-marks-ML/main/dataset_marks.txt"
s_data= pd.read_csv(url)
print("data imported successfully")
s_data.head(10)

#plot graph of score
s_data.plot(x='Hours',y='Scores',style='o')
plt.title('Hours vs Scores')
plt.xlabel('Hours studied')
plt.ylabel('percentage score')
plt.show()

"""positive relation between hours and marks scored"""

#preparing data
x=s_data.iloc[:,:-1].values
y=s_data.iloc[:,1].values

y,x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#train the algorithm
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print('training complete')

#plot the regression line
line=regressor.coef_*x+regressor.intercept_

#plotting test data
plt.scatter(x,y)
plt.plot(x,line);
plt.show()

#making predictions
print(x_test)    #test data
y_pred=regressor.predict(x_test)

#comparing actual vs predicted
df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
df

#accuracy
Score_pred=np.array([9.25])
Score_pred=Score_pred.reshape(-1,1)
predict=regressor.predict(Score_pred)
print('number of hours={}'.format(9.25))
print('predicted score={}'.format(predict[0]))

#evaluate
from sklearn import metrics
print('Mean Absolute Error :',
      metrics.mean_absolute_error(y_test,y_pred))