import types
types.ModuleType

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from pandas.plotting import register_matplotlib_converters

# import seaborn as sns
register_matplotlib_converters()

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

sns.set_palette("Set2", 8)
sns.set_context("notebook", font_scale=1.5)
 
import sys
sys.path.append("../")
import makedata

# For the notebook
