import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import time
import datetime
import re
import json
import logging
import logging.config
import logging.handlers
import traceback
import subprocess
import threading
import multiprocessing
from multiprocessing import Process, Queue, Pool
from multiprocessing.managers import BaseManager

from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pre
