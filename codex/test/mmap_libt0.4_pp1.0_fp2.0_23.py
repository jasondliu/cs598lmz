import mmap
import os
import re
import sys
import time

from collections import defaultdict
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from optparse import OptionParser
from os.path import basename
from os.path import dirname
from os.path import exists
from os.path import join
from os.path import realpath
from os.path import splitext
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError
from subprocess import PIPE
from subprocess import Popen
from subprocess import STDOUT
from tempfile import NamedTemporaryFile
from tempfile import mkdtemp
from tempfile import mkstemp

