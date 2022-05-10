import mmap, json, sys, re, time
from functools import partial
import traceback, types
from inspect import getframeinfo, stack
from itertools import tee
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import Process as ThreadProcess
from collections import defaultdict
from collections import OrderedDict
from tqdm import tqdm
from string import ascii_lowercase
from datetime import datetime

infile=sys.argv[1]
bam_name=sys.argv[2]
ref_file=sys.argv[3]
th=sys.argv[4]
json_outfile=sys.argv[5]
strain_outfile=sys.argv[6]

import parsing_functions as pf
import mip_functions as mip
import variant_identification_functions as vif
from operator import itemgetter
from sklearn.cluster import DBSCAN

from multiprocessing import Pool, Manager, Process

