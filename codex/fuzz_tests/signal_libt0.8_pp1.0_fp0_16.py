import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
#
import os
import imp
import sys
import time
import datetime
import traceback
import cPickle as pickle
import collections
import re

# check the versions of some important libraries
## import pkg_resources
## assert pkg_resources.get_distribution("rootpy").version >= "0.7.1"
## assert pkg_resources.get_distribution("pandas").version >= "0.23.1"
## assert pkg_resources.get_distribution("numpy").version >= "1.14.2"
## assert pkg_resources.get_distribution("uproot3").version >= "3.0.0"
#
# load additional libraries from a local directory 'pylib'
if os.path.exists('pylib'):
    sys.path.insert(0, 'pylib')

import ROOT
import json
import math
import uproot3 as uproot
import numpy as np
import pandas as pd
import root_
