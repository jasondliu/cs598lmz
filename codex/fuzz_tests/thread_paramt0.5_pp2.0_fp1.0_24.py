import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn-whitegrid')
#%%
import sklearn.datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
#%%
X, y = sklearn.datasets.make_regression(n_samples=500, n_features=1, noise=10)
X = X.flatten()
y = y.flatten()
#%%
plt.scatter(X, y, s=5)
#%%
print(f'X.shape={X.shape}, y.shape={y.shape}')
#%%
X = X.reshape(-1, 1)
y = y.reshape(-1,
