import ctypes
ctypes.windll.kernel32.SetDllDirectoryW(None) # Reset it
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patch as mpatches
import numpy as np
import pandas as pd
import statistics as st

from datetime import date, datetime, timedelta
from scipy.stats import chisquare, chi2_contingency
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


from statsmodels.tsa.ar_model import AR, ARResults
from statsmodels.tsa.arima_model import ARMA, ARMA, ARIMA 
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_
