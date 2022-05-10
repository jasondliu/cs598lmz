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

from build_utils import *

#------------------------------------------------------------------------------
# Globals
#------------------------------------------------------------------------------

# The top-level directory of the source tree.
SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# The directory where the build artifacts are placed.
BUILD_ROOT = os.path.abspath(os.path.join(SOURCE_ROOT, 'out', 'Release'))

# The directory where the build artifacts are placed.
BUILD_ROOT_DEBUG = os.path.abspath(os.path.join(SOURCE_ROOT, 'out', 'Debug'))

# The directory where the build artifacts are placed.
BUILD_ROOT_RELWITHDEBINFO = os.path.abspath(os.path.join
