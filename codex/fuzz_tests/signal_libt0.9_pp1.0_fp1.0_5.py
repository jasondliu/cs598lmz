import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)

import logging
import gensim
import gensim.corpora as corpora
from pyLDAvis import (
    # gensim as gensim_vis,
    gensim as gensim_vis,
    prepare as vis_prepare,
)


# In[2]:


import os
datapath = os.path.join(os.getenv('HOME', ''), 'data/corsera/')
pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger()


# In[6]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
pp.pprint(stop_words)


# In[3]:


def load_dataset(datapath):
    # global vect_train, vect_test, lem_train, lem_test
    global df_lda

    #
