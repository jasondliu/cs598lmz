from bz2 import BZ2Decompressor
BZ2Decompressor()  # this is necessary for some reason

import gzip
import logging

from collections import defaultdict, Counter
from itertools import product
from optparse import OptionParser
from urllib.parse import urlparse

import numpy as np
