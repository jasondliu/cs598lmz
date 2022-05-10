import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import numpy as np
import sys
import pandas as pd

from constants import CATEGORIES, SITE_ROOT, USE_CATEGORIES


def load_corpus():
    '''
        Loads the data from the corpus and returns it as a pandas data frame
    '''
    filename = SITE_ROOT+'\\corpus\\data_nk5_g2.csv'
    data = pd.read_csv(filename, sep='#', encoding="utf8")
    data = data.dropna(axis=0, thresh=13)
    data.text = data.text.astype(str)
    return data

def remove_false_category(old_category):
    '''
        Filters out the newlines and other characters, that are in the categories.
    '''
    false_chars = ["\n", "\\", "/", "[", "]", "'", ",", "
