from lzma import LZMADecompressor
LZMADecompressor()

from io import BytesIO

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping


# In[2]:


# Load the data

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/satimage/sat.trn"
s = requests.get(url).content
s = LZMADecompressor().decompress(s)
df = pd.read_csv(BytesIO(s), sep=' ', header=None)
