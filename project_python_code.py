
# coding: utf-8

# In[37]:


#import the required libraries
import pandas as pd
import numpy as np
get_ipython().magic(u'matplotlib inline')
from datetime import datetime
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
from scipy import stats
import statsmodels.api as sm
import warnings
from itertools import product
from datetime import datetime
warnings.filterwarnings('ignore')
plt.style.use('seaborn-poster')


# In[38]:


matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


# In[83]:


#https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython
#https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
#data.drop(<axis name>, axis = 1) #delete a column
#https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
data = pd.read_excel("project_dataset.xlsx", sheet_name="Sheet1",parse_dates=["Date"], index_col = "Date", data_parser = lambda dates: pd.datetime.striptime('%Y-%m-%d')).drop("Unnamed: 6", axis = 1)
data = data[['Total stock','Australia','Brazil','India','Other']]
print(data.head())
print('\n Data Types:')
print(data.dtypes)
print(data.describe())
print(len(data))


# In[40]:


print(data.index)
print('First date:', data.index.min())
print('Last date:', data.index.max())


# In[43]:


data.plot(figsize=(15, 6))


# In[44]:


data.hist()


# In[42]:


#https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
sm.tsa.seasonal_decompose(data, freq=52).plot()


# In[13]:


#https://www.dummies.com/programming/big-data/data-science/autocorrelation-plots-graphical-technique-for-statistical-data/
pd.plotting.autocorrelation_plot(data)


# In[14]:


#Prediction:


# In[80]:


#Function that calls ARIMA model to fit and forecast the data
def StartARIMAForecasting(Actual, P, D, Q):
	model = ARIMA(Actual, order=(P, D, Q))
	model_fit = model.fit(disp=0)
	prediction = model_fit.forecast()[0]
	return prediction
    
#Get exchange rates
ActualData = data['Total stock'].values
#Size of exchange rates
NumberOfElements = len(ActualData)

#Use 90% of data as training, rest 30% to Test model
TrainingSize = int(NumberOfElements * 0.90)
TrainingData = ActualData[0:TrainingSize]
TestData = ActualData[TrainingSize:NumberOfElements]

#new arrays to store actual and predictions
Actual = [x for x in TrainingData]
Predictions = list()


#in a for loop, predict values using ARIMA model
for timepoint in range(len(TestData)):
	ActualValue =  TestData[timepoint]
	#forcast value
	Prediction = StartARIMAForecasting(Actual, 4,1,0)    
	#print('Actual=%f, Predicted=%f' % (ActualValue, Prediction))
	#add it in the list
	Predictions.append(Prediction)
	Actual.append(ActualValue)

#Print MSE to see how good the model is
#Error = MeanSquaredError(TestData, Predictions)
#print('Test Mean Squared Error (smaller the better fit): %.3f' % Error)
# plot
plt.plot(TestData)
plt.plot(Predictions, color='red')
plt.show()
