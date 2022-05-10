import select
import sys
import time

import numpy as np
import scipy.io

sys.path.insert(0, '../../src')
import localmodule


# Define constants.
dataset_name = localmodule.get_dataset_name()
