import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Importing the libraries
import numpy as np # for mathematical operations
import matplotlib.pyplot as plt # for plotting
import pandas as pd # for importing and managing datasets

# Importing the dataset
dataset = pd.read_csv('train.csv')
dataset.head()

dataset['text'][0]

dataset['keyword'][0]

dataset['target'][0]

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i]) # remove everything except alphabets
    review = review.lower() # converting to lowercase

