import bz2
bz2.BZ2File.read = lambda self, size=-1: self.readline()

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Open the data file
data = bz2.BZ2File('train.ft.txt.bz2')
# Read the first line of the data file
line = data.readline()
# Print the first line of the data file
print(line)

# Convert the first line to a string, split it on spaces, and return the second element
line.decode("utf-8").split(" ")[1]

# Convert the first line to a string, split it on spaces, and return the first element
line.decode
