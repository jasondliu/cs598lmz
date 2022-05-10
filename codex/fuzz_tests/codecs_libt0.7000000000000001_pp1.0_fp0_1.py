import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import seaborn as sns

import json
import re

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import utils

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

sns.set_style("darkgrid")

np.random.seed(42)

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', 150)

pd.set_option('display.precision', 3)

pd.options.display.max_colwidth=100

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from
