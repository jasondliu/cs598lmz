import mmap
import os
import sys

from couchdb.client import Document, Database, Server
from matplotlib.dates import date2num
from matplotlib.offsetbox import AnchoredText
import numpy as np
import pylab as plt
from scipy.interpolate import interp1d

from data import DATA_TYPES

# Colors from the colorbrewer scheme (type 'qualitative' | nb classes: 7)
colors = [ '#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f' ]

# Start up with some command line arguments
neighbor_id = sys.argv[1]
