import threading
threading.stack_size(67108864) # 64MB stack
#@title ...import all libraries

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown
import matplotlib.image as mpimg

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import re
# import shutil
from tqdm import tqdm
from sklearn.manifold import TSNE

# word2vec
import gensim
import multiprocessing

# keras
from keras import backend as K
import tensorflow as tf

from keras.preprocessing import sequence
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, LSTM, Input
from keras.layers.normalization import BatchNormalization
from keras.optimizers import RMSprop, Adam

# nltk
import nltk
