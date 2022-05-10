import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from functools import partial
from itertools import chain
from itertools import groupby
from itertools import islice
from itertools import tee
from operator import itemgetter
from optparse import OptionParser
from os.path import basename
from os.path import dirname
from os.path import exists
from os.path import join
from os.path import splitext
from os.path import split
from os.path import abspath
from os.path import normpath
from os.path import realpath
from os.path import relpath
from os.path import expanduser
from os.path import isabs
from os.path import isdir
from os.path import isfile
from os.path import islink
from os.path import getsize
from os.path import getmtime
from os.path import getatime
from os.path import getctime
from os.path import lexists
from os.path
