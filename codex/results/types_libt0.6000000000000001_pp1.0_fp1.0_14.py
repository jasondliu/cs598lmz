import types
types.ModuleType.__repr__ = lambda self: self.__name__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc

from scipy import interp
from itertools import cycle

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

pd.set_option('display.max_columns', 500)
 
# Load the data
df = pd.read_csv('data/dataset.csv')
 
df.head()

# In this notebook we will be performing a logistic regression using a dataset of a telecommunication company. We have the customer information, if they churned or not as well as some services that they have signed up for.

# In[2]:


# Check the data types
