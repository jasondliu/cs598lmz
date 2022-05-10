import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import os
import sys
import re
import scipy.io as sio
import scipy.stats as stats
import math
import random
import copy

#from sklearn.metrics import mean_squared_error
#from sklearn.metrics import mean_absolute_error

#from sklearn.cluster import KMeans
#from sklearn.cluster import DBSCAN
#from sklearn.cluster import AgglomerativeClustering
#from sklearn.neighbors import kneighbors_graph
#from sklearn.cluster import Birch
#from sklearn.cluster import SpectralClustering
#from sklearn.cluster import AffinityPropagation
#from sklearn.cluster import MeanShift
#from sklearn.cluster import estimate_bandwidth
