import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from subprocess import Popen, PIPE

