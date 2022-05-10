import mmap
import os
import re
import sys

from collections import defaultdict
from collections import OrderedDict
from itertools import groupby
from operator import itemgetter

import numpy as np
import pandas as pd

from Bio import SeqIO
