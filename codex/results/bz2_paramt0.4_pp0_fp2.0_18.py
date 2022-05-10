from bz2 import BZ2Decompressor
BZ2Decompressor

# In[ ]:

import os
import sys
import csv
import re
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

# In[ ]:

# Load data
print("Loading data...")
# load training data
train_df = pd.read_csv("../input/train.csv")
test_df = pd.read_csv("../input/test.csv")

# In[ ]:

# Clean data
print("Cleaning data...")
# remove constant columns
colsToRemove = []
for col in train_df.columns:
    if train_df[col].std() == 0:
        colsToRemove.append(col)

train_df.drop(
