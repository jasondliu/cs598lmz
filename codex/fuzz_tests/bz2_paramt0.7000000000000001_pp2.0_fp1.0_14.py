from bz2 import BZ2Decompressor
BZ2Decompressor()  # this is necessary for some reason

import gzip
import logging

from collections import defaultdict, Counter
from itertools import product
from optparse import OptionParser
from urllib.parse import urlparse

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

logging.basicConfig(level=logging.INFO)

optparser = OptionParser()
optparser.add_option("--input", dest="input", default="ctakes-output.txt.gz", help="output file from cTAKES")
optparser.add_option("--output", dest="output", default="ctakes-output-sorted.txt.gz", help="output file to write sorted data to")
optparser.add_option("--pca", dest="pca", default=None, help="output file for PCA analysis")
optparser.add_option("--k
