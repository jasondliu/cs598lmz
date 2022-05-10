import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import datetime
#from fbprophet import Prophet
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('C:/Users/ankur/Desktop/data_science_practice/datasets/COVID-19/covid_19_clean_complete.csv',parse_dates=['Date'])
df.head()

df.rename(columns={'ObservationDate':'Date', 'Country/Region':'Country'}, inplace=True)

#df.head()

df_confirmed = pd.read_csv("C:/Users/ankur/Desktop/data_science_practice/datasets/COVID-19/time_series_covid_19_confirmed.csv")
df_recovered = pd.read_csv("C
