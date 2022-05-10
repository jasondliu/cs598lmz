import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
from pytrends.request import TrendReq
pytrend = TrendReq()
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
nltk.download('stopwords')
nltk.download('punkt')
import re
import operator
from math import log
from operator import itemgetter
import json
from nltk.stem.snowball import SnowballStemmer
from math import log


# ## Part 1: Setting up environment

# In[2]:


# list of dates for which you want to do the regularity analysis. The length of this list determines the number of iterations
# if you want to do your analysis for 7 days from today, use datetime.now().date() as the beginning date.
dates = [datetime.date(2018,1,1), datetime
