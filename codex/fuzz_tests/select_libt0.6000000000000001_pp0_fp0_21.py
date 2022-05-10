import select
import sys
import time

import numpy as np
import scipy.io

sys.path.insert(0, '../../src')
import localmodule


# Define constants.
dataset_name = localmodule.get_dataset_name()
args = ["unit01", "unit02", "unit03", "unit05", "unit07", "unit10", "unit11", "unit12", "unit13", "unit14", "unit15", "unit16", "unit17", "unit18", "unit19", "unit20", "unit21", "unit22", "unit23", "unit24", "unit25", "unit26", "unit27", "unit28", "unit29", "unit30", "unit31", "unit32", "unit33", "unit34", "unit35", "unit36", "unit37", "unit38", "unit39", "unit40", "unit41", "unit42", "unit43", "unit44", "unit45", "unit46", "unit47", "unit48", "unit49", "unit50", "unit51",
