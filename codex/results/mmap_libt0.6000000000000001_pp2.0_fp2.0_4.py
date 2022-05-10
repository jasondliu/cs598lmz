import mmap
import numpy as np
import os
import re
import scipy.stats as st
import sys

from collections import Counter, defaultdict
from os.path import join as pjoin

# sys.path.insert(0, '/home/arash/git/scripts/')
sys.path.insert(0, '/home/arash/git/kaldi-io-for-python/')
import kaldi_io

# sys.path.insert(0, '/home/arash/git/pytorch-kaldi/')
# from utils import *

try:
    import ujson as json
except ImportError:
    import json

try:
    import cPickle as pickle
except ImportError:
    import pickle

# import sys
# sys.path.insert(0, '/home/arash/git/pytorch-kaldi/')

# import kaldi_io
# import numpy as np
# import torch
# import torch.nn.functional as F
# from torch.autograd import Variable
# from torch.utils.data import Dat
