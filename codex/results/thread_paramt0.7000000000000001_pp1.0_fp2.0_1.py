import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()


# In[24]:


# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys, threading

# Importing datetime 
import datetime as dt

# Importing warnings
import warnings

# Importing statsmodels
import statsmodels.api as sm

# Importing itertools
import itertools

# Importing pmdarima
import pmdarima as pm

# Importing Prophet
from fbprophet import Prophet

# Importing adfuller
from statsmodels.tsa.stattools import adfuller

# Importing ARIMA
from statsmodels.tsa.arima_model import ARIMA

# Importing ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Importing seasonal_decompose
from statsmodels.tsa.seasonal import seasonal_decompose

# Importing itertools
import it
