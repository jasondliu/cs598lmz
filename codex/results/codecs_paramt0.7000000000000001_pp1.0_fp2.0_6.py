import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

# Python 2/3 compatibility
from six import with_metaclass
from six.moves import zip
from six.moves import range
import six

# Numpy
import numpy as np

# Fastcluster
try:
    from fastcluster import linkage
except ImportError:
    print("Fastcluster not available. You may want to install it to improve performance.")
    from scipy.cluster.hierarchy import linkage

# Scipy
from scipy.cluster.hierarchy import _average_neighbor_distance
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import find_clusters
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
from scipy.stats import pearsonr

# Pandas
import pandas as pd

# Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

