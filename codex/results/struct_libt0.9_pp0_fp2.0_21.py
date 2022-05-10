import _struct
import copy
import glob
import math
import operator
import os
import pprint
import re
import shutil
import sys
import time

import numpy as np

if sys.version_info.major == 2:
    from urllib2 import urlretrieve
else:
    from urllib.request import urlretrieve

# Pass and fail counters
_PASS = 0
_FAIL = 0

# Tolerance for comparing floating
_TOLERANCE = 1e-6

# Tolerance for comparing floating in precision mode
_TOLERANCE_LOW_PRECISION = 1e-4

# Path to the tools directory
_TOOLS_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..',
                                           'tools'))

# Global debug level
_DEBUG = 0

# Supress py3 static analysis warnings
if sys.version_info.major == 3:
    _TOOLS_PATH = None
