import mmap
import os
import re
import sys

from collections import OrderedDict
from distutils.spawn import find_executable
from io import StringIO
from subprocess import Popen, PIPE

