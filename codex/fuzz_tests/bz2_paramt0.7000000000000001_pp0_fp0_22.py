from bz2 import BZ2Decompressor
BZ2Decompressor
from multiprocessing import Pool
from joblib import Parallel, delayed
import multiprocessing
import os
from multiprocessing import Process
import datetime as dt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from pandas.core.dtypes.dtypes import CategoricalDtype
from collections import Counter
from itertools import chain
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_curve
from sklearn
