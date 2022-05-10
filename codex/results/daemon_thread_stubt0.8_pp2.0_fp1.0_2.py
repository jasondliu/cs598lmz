import sys, threading

def run():
    sys.exit(subprocess.call(['open', '-a', 'Simulator']))
threading.Thread(target=run).start()
sleep(5)
print('Simulator started.')

import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')

df = web.DataReader('AMZN','google',start,end)

df['Adj Close'].plot(legend=True,figsize=(10,4))
plt.ylabel('Adj Close')
plt.show()

df['HL_PCT'] = (df['High'] - df['Close']) / df['Close'] * 100.0
df['PCT_
