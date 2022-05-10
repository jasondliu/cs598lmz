import mmap
from collections import defaultdict
from contextlib import contextmanager
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from operator import itemgetter
from os import path, makedirs
from typing import Iterable, List, Tuple, Union, Optional

from numpy import array, mean, std, percentile, savez, load
from pandas import DataFrame, read_csv, concat, Series, read_hdf
from scipy.sparse import csr_matrix, save_npz, load_npz
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

from .utils import (
    get_logger,
    get_data_path,
    get_data_file_path,
    get_cache_file_path,
    get_output_file_path,
    get_output_path,
    get_cache_path,
    get_
