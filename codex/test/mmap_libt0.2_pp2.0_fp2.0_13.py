import mmap
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from subprocess import Popen, PIPE

import numpy as np
import pandas as pd
from scipy.stats import entropy
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from utils import *

# Set random seed
np.random.seed(42)

# Set global variables
