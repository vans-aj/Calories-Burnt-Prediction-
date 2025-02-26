#imporing the dependencies
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;
from sklearn.model_selection import train_test_split;
from xgboost import XGBRegressor;
from sklearn import metrics;

# taking data set
calories = pd.read_csv('calories.csv')
exercise = pd.read_csv('exercise.csv')

# merging the data
data  = pd.concat([exercise,calories['Calories']],axis=1)

# analysing the data
data.shape
data.info()
data.isnull().sum()
data.describe()

# visualizing the data
sns.set()
sns.countplot(data['Gender'])
#finding the distribution of age
sns.distplot(data['Age'])
#finding the distribution of height
sns.distplot(data['Height'])
#finding the distribution of weight
sns.distplot(data['Weight'])
#finding the distribution of duration
sns.distplot(data['Duration'])


#finding the corelation
correlation = data.select_dtypes(include=np.number).corr(); 
# Select only numerical columns before calculating correlation
#constructing the heatmap to understand the corelation
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Reds')

#converting text data to neumerical values
data.replace({"Gender": {'male':0,'female':1}}, inplace =True)

#seprating feature and and target
X = data.drop(columns=['User_ID','Calories'],axis=1)
Y = data['Calories']

#splitting the data into test and train
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

#model training
model = XGBRegressor()
model.fit(X_train,Y_train)

#evalution
#prediction of test data
prediction = model.predict(X_test)

#mean absolute error
mae = metrics.mean_absolute_error(Y_test,prediction)
print(mae)