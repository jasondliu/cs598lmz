import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import argparse
import os
import uuid
import glob
import re
import time

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from matplotlib.backends.backend_pdf import PdfPages

import scipy
from scipy.stats import spearmanr
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list, optimal_leaf_ordering
from scipy.spatial.distance import squareform, pdist

import pr_util

def main(args):
    """main function"""

    # pickle the args
    pickled_args_fn = '%s.args.pickle' % args.out_prefix
    pr_util.pickle_obj(args, pickled_args_fn)

    # load the matrix
    tab_df =
