import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import argparse
from os import listdir
from os.path import isfile, join
import sys
import librosa
import librosa.display
import os
import re
import matplotlib.pyplot as plt
import logging
from pydub import AudioSegment
import numpy as np
from scipy import signal
import scipy
import scipy.io.wavfile
import scipy.signal
import scipy.fftpack
import math
import operator
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn
