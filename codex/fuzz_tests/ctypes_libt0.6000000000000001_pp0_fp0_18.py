import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from plotnine import *

import os
from pathlib import Path
import sys
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Import utils
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from utils import *

# Set seed for reproducibility
np.random.seed(0)
 
# Set plotting style
plt.style.use('fivethirtyeight')

# Increase default plot size and set default text sizes
plt.rcParams['figure.figsize'] = (12, 9)
plt.rcParams['font.size'] = 18

# Disable scientific notation for pandas
pd.set_option('display.float_format', lambda x: '%.3f'
