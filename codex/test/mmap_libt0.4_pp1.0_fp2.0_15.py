import mmap
import os
import re
import sys

from collections import defaultdict
from glob import glob
from os.path import abspath, basename, dirname, expanduser, getsize, isdir, isfile, join, splitext
from subprocess import Popen, PIPE

