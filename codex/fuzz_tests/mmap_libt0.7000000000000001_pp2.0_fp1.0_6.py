import mmap
import sys
import os
import time
 
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer

####################################################################################################################
# The following functions are helpers for the main functions in this file.
####################################################################################################################

def get_file_size(file_name):
    """
    Returns the size of a file in bytes.
    """
    return os.path.getsize(file_name)

def get_directory_size(directory_name):
    """
    Returns the size of a directory in bytes.
    """
    size = 0
    for (path, dirs, files) in os.walk(directory_name):
        for file in files:
            size += os.path.getsize(os.path.join(path, file))
    return size

def get_mmap(file_name, file_size):
    """
    Returns an mmap of the given file with size file_size.
    """
    return mmap.mm
