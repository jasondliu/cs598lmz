import mmap
import math
import sys
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle

# Takes in a list of strings and returns a string of the concatenated list
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

# Takes in a file and returns a parsed list of strings of each line in the file
def parse_file(file):
    data = []
    with open(file, encoding="utf8") as f:
        for line in f:
            data.append(line)
    return data
