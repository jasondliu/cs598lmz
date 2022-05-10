import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# scikits-learn 1.1.0rc1-g77a3bcc is required
#import matplotlib as mpl
#mpl.use('Agg')
#import matplotlib.pyplot as plt

import numpy as np

import sklearn.datasets as skdat
import sklearn.metrics as skmet
import sklearn.preprocessing as skpre
import sklearn.pipeline as skpipe
import sklearn.dummy as skdum
import sklearn.feature_extraction.text as skfeat
import sklearn.linear_model as sklm
import sklearn.ensemble as skle
import sklearn.grid_search as skgs


################################################################################
# General helper functions
################################################################################

def entropy(c):
    """Calculate the Shannon entropy of a set of labels.
    """
    n = len(c)
    u = len(np.unique(c))

    # logarithm base 2
    base = 2

    if u == 1:
        # entropy
