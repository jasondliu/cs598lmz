import mmap
import numpy as np
import os
import pickle
import sys
import time

from gensim.models import word2vec
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split

from data_utils import *
from config import *

# from tensorflow.python import debug as tf_debug

# from tensorflow.python.tools import inspect_checkpoint as chkp

# from tensorflow.python import debug as tf_debug

# from tensorflow.python.tools import inspect_checkpoint as chkp

# from tensorflow.python.tools import freeze_graph

# from tensorflow.python.tools import optimize_for_inference_lib

# from tensorflow.tools.graph_transforms import TransformGraph

# from tensorflow.python.tools import optimize_for_inference_lib

# from tensorflow.tools.graph_transforms import TransformGraph

# from tensorflow.python.tools import freeze_graph

# from tensorflow.python.
