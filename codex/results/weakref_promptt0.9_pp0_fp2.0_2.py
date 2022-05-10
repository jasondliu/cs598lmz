import weakref
# Test weakref.ref
x = 42
x_wr = weakref.ref(x)
print (x_wr())


joints = [None, None, 0]
print (type(joints[0]))

def fft(x):  
    N = len(x)
    X = np.ceil(np.log2(N))
    X = int(2**X)
    y = np.zeros(X)
    y[0:N]=x
    return np.fft.fft(y)

x = np.linspace(0, 5, 10)
print (x)
print (fft(x))


import numpy as np
import pandas as pd
from matplotlib import dates
import matplotlib.dates as mdates
import datetime
from datetime import datetime
import matplotlib.pyplot as plt

def df_convert_time_and_plot(df, timeFrom, title):
    df["time"] = pd.to_datetime(df["time"], format=timeFrom)
    df = df
