import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from subprocess import Popen, PIPE

