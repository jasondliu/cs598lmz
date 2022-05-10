import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile

from optparse import OptionParser

from util import build_utils
from util import md5_check
from util import resource_utils
from util import system_utils

# Path constants. (All of these should be absolute paths.)
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
SDK_SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', '..', '..'))
SDK_EXAMPLES_DIR = os.path.join(SDK_SRC_DIR, 'examples')
SDK_OUT_DIR = os.path.join(SDK_SRC_DIR, 'out')
SDK_LIB_DIR = os.path.join(SDK_OUT_DIR, 'lib')
SDK_GEN_DIR = os.path.join(SDK
