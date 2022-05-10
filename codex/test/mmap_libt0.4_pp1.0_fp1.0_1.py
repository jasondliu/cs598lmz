import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from itertools import chain
from operator import itemgetter
from optparse import OptionParser
from pprint import pprint
from subprocess import Popen, PIPE

