from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("../data/publicChallenge.csv.bz2", "rb").read())

#%% [markdown]
# ### Load the training data from train.csv into a pandas DataFrame.

#%%
import numpy as np
import pandas as pd

with open("../data/publicChallenge.csv", "rb") as f:
    train = pd.read_csv(f, header=None)

#%% [markdown]
# ### Load the testing data from test.csv into a pandas DataFrame.

#%%
with open("../data/publicChallengeTest.csv", "rb") as f:
    test = pd.read_csv(f, header=None)


#%%
# split into X and y
train_X = train.iloc[:, :-1]
train_y = train.iloc[:, -1]

test_X = test.iloc[:, :-1]
test_y = test.iloc[:, -1]

#%%
from sklearn.preprocessing import Imputer
