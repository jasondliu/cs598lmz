import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import string
import re
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import nltk
from collections import Counter
import os
import sys
import time
import logging
import time
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.utils import shuffle

from textblob import TextBlob

from sklearn
