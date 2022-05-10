import lzma
lzma.LZMAFile

import numpy as np
import scipy.sparse
import scipy.sparse.linalg
import scipy.spatial.distance

import pandas as pd
import sklearn.metrics
import sklearn.preprocessing

import matplotlib.pyplot as plt
import seaborn as sns

import argparse

import logging
logger = logging.getLogger(__name__)
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--in_file', required=True)
    parser.add_argument('--out_file', required=True)

    parser.add_argument('--n_neighbors', type=int, default=10)
    parser.add_argument('--metric', default='euclidean')
    parser.add_argument('--n_components', type=int, default=2)
    parser.add_argument('--alpha', type=float, default=0.5)
    parser.add_argument('--min_
