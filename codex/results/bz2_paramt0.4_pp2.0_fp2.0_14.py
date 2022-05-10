from bz2 import BZ2Decompressor
BZ2Decompressor

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gc
import warnings
warnings.filterwarnings('ignore')

# In[ ]:


from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder

# In[ ]:


import lightgbm as lgb

# In[ ]:


import os
os.listdir('../input')

# In[ ]:


from sklearn.metrics import roc_auc_score

# In[ ]:


def get_data_frame(filename):
    with bz2.BZ2File(filename) as f:
        file_content=f.read()
        decompressor=BZ2Decompressor()
        decompressed_content=decompressor.decompress(file_content)
        return pd.read_csv(io.StringIO(decompressed_content
