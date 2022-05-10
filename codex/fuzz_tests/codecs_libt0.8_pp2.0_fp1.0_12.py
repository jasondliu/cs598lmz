import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
# from __future__ import division, print_function
# import sys
# import itertools
# import multiprocessing as mp
# from operator import itemgetter, attrgetter

import cyvcf2

# import gzip
import argparse
# import time
# import re
import sys
# import math
# import pdb
# import os
# import copy
# import ntpath
#import re
import io
import stat
# import json
import warnings
warnings.filterwarnings("ignore")
import multiprocessing
from multiprocessing.pool import ThreadPool

import os
scriptpath = os.path.dirname(os.path.realpath(__file__))

# import pdb
# import scipy.stats as ss
# import numpy as np

# from collections import Counter
# from collections import defaultdict
# from collections import OrderedDict

#########################################################
class MultiprocessingWorker(mult
