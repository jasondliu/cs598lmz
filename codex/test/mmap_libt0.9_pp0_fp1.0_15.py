import mmap
import numpy as np
from glob import glob
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Bidirectional
from keras.utils import plot_model
from keras.models import load_model

def get_count(file, grammar=re.compile(r'[,.!?()"]')):
    '''
    A function to count the number of lines
    in a file.

    param: str
    return: int
    '''
    text = open(file, 'r+')
    return sum(bl.count('\n') for bl in mmap.mmap(text.fileno(), 0, access=mmap.ACCESS_READ))    
