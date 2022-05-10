import bz2
bz2.BZ2File.close = lambda self: None  # Ignore bz2 close()
import gzip
gzip.GzipFile.close = lambda self: None  # Ignore gzip close()
import os
import sys
import subprocess
from distutils.spawn import find_executable
from distutils.version import LooseVersion
from multiprocessing.pool import ThreadPool

import numpy as np
import pandas as pd

from . import constants
from . import utils
from . import config
from . import exceptions
from . import data
from . import features
from . import plotting
from . import estimators
from . import metrics
from . import model_selection
from . import visualization
from . import preprocessing
from . import impute
from . import compose
from . import feature_selection
from . import feature_extraction
from . import multiclass
from . import workload
from . import _load_data
from . import _load_features
from . import _load_model
from . import _load_metrics
from . import _load_estimators
from . import _load_model
