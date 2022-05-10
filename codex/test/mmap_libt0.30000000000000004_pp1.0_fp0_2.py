import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from optparse import OptionParser
from subprocess import Popen, PIPE

