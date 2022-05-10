import codecs
codecs.register_error('strict', codecs.ignore_errors)

# for removing diacritics
import unicodedata

# for error-checking
import errno

# for sys.exit
import sys

# for logging
import logging

# for 
import english_contractions_dictionary

# for removing stopwords
import stopwords_list

# for lemmatizing
from nltk.stem import WordNetLemmatizer

# for stemming
from nltk.stem.porter import PorterStemmer

# for removing punctuation
import string

# for tokenizing
from nltk.tokenize import word_tokenize

# for making a directory
import os

# for getting the current date and time
from datetime import datetime

# for reading the CSV files
import csv

def remove_diacritics(text):
    """
    Removes diacritics from a text.
    """
    normalized_text = unicodedata.normalize('NFKD', text)
    return normalized_text.encode('ascii', 'ignore')
