import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from operator import itemgetter
from os.path import basename, dirname, exists, isdir, isfile, join
from subprocess import check_output, CalledProcessError
from threading import Lock

