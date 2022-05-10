import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import sys, urllib, json, os
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline


# ## Config

# In[874]:

endpoint = 'https://api.twitter.com/1.1/search/tweets.json'
# # Replace these three values with your own values
# keywords = ['#대통령'] # the hashtag which you want to know the sentiment
# keywords = ['#PK', '#김정은대통령', '#김정은', '#김정음대통령', '#김정음']

# keywords = [
#             '#세월호', '#세월호참사', '법
