from bz2 import BZ2Decompressor
BZ2Decompressor()


# In[10]:

file=bz2.BZ2File(train_path, 'r')
train_raw=file.readlines()
file_test=bz2.BZ2File(test_path, 'r')
test_raw=file_test.readlines()


# In[12]:

train_raw[0:5]


# In[13]:

test_raw[0:5]


# In[14]:

df=pd.DataFrame(train_raw)
df.head()


# In[15]:

type(df)


# In[16]:

df2 = pd.DataFrame(test_raw)
df2.head()


# In[17]:

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabel
