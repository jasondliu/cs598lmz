import lzma
lzma.open

import numpy as np
import numpy.linalg as linalg
import random as rand
from random import randint
import sys

import os
import pickle
import shutil

from lxml import etree
import tarfile as tar
from datetime import datetime
import re

from tqdm import tqdm

import scipy.spatial.distance as sp_dist
import scipy.io.wavfile as wavfile
from scipy.fftpack import dct
from scipy import signal
from scipy.signal import correlate


from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.met
