import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain, groupby
from operator import attrgetter
from optparse import OptionParser
from os.path import abspath, basename, dirname, exists, isdir, isfile, join
from shutil import rmtree
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from threading import Thread
from time import sleep
from xml.etree import ElementTree

