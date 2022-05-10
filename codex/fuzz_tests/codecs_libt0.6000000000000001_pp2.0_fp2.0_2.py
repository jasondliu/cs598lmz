import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import string
import sys
import os
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data
df = pd.read_csv('C:\\Users\\matt\\Desktop\\output.csv', encoding='utf-8')
# clean the data
df = df.drop(['Unnamed: 0'], axis=1)
df = df.drop(['Date'], axis=1)
df = df.drop(['Time'], axis=1)
df = df.drop(['location'], axis=1)
df = df.drop(['tweets'], axis=1)
df = df.drop(['replies'], axis=1)
df = df.drop(['retweets'], axis=1)
df = df.drop(['likes'], axis=1)
df =
