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

from distutils.version import LooseVersion
from optparse import OptionParser

# This is not the version of the script, but the version of the
# package that the script is intended to build.
#
# This is used to determine the name of the package.
PACKAGE_VERSION = "2.0.0"

# This is the version of the script itself.
SCRIPT_VERSION = "2.0.0"

# The directory where this script is located.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# The root of the source tree.
SOURCE_ROOT = os.path.dirname(SCRIPT_DIR)

# The root of the build tree.
BUILD_ROOT = os.path.join(SOURCE_ROOT, "build")

# The root of the package tree.
PACK
