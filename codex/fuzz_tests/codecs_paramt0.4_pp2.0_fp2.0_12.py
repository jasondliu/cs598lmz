import codecs
codecs.register_error('strict', codecs.ignore_errors)

from collections import Counter
from collections import defaultdict
import csv
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import glob
import itertools
import json
import math
import matplotlib.pyplot as plt
import numpy as np
import operator
import os
import pandas as pd
import random
import re
import scipy.stats as stats
import seaborn as sns
import string
import sys
import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import NMF
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.
