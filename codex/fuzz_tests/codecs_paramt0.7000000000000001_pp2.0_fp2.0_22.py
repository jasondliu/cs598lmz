import codecs
codecs.register_error('strict', codecs.ignore_errors)

from dask.bag import Bag
from dask.diagnostics import ProgressBar
from dask.distributed import Client
from dask_jobqueue import SLURMCluster
from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler

from dateutil import parser

from fastparquet import ParquetFile

from geopy.distance import geodesic

from glob import glob

import hdbscan
from hdbscan import HDBSCAN

from importlib import reload
import IPython
import json

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.tri as tri

from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.colors import to_hex

from matplotlib.dates import date2num, num2date
from matplotlib.path import Path
from matplotlib.ticker import AutoMinorLocator

from mpl_toolkits
