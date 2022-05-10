import codecs
codecs.register_error('strict', codecs.lookup_error('surrogateescape'))

# this is a test of the git set up

# my comment to test the github pull request
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# for qc reports
from IPython.display import display, HTML

import urllib.request

# display plots in the notebook
%matplotlib inline

# increase default figure and font sizes for easier viewing
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14

# import the csv file into a pandas dataframe

# df = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD', encoding = 'utf-8')
# df = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.
