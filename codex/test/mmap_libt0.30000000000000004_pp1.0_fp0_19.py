import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from itertools import chain
from optparse import OptionParser
from os.path import dirname, join, realpath
from subprocess import Popen, PIPE
from threading import Thread

