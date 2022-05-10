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

