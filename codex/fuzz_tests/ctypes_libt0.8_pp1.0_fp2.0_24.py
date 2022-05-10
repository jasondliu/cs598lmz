import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# %% [markdown]
# ### Importing relevant libraries

# %%
import os
print(os.getcwd())
import sys
import json
import pandas as pd
import numpy as np
import matplotlib
import cytoolz
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
from copy import deepcopy

# %% [markdown]
# These are the relevant files

# %%
# Getting the relevant files
sys.path.insert(0, "../../../utils/student_caller")
sys.path.insert(0, "../../../utils/mooc_relational_inference")

from relational_inference_calls import load_dataset, \
                                         split_dataset, \
                                         get_dataset_stats

from backprop_relational import train_model, \
                                compute_gradients, \
                                compute_gradients_log, \
                                backprop_step

