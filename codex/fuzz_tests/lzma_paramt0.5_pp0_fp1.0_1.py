from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, memlimit=None, filters=None)

# The following three lines are a workaround to the issue described here:
# https://github.com/pypa/pip/issues/6164
# If we don't do this, pip will fail to install the dependencies.
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

# We need to import the global variables in order to
# use them in the following imports.
from . import global_vars

# This is a workaround for the issue described here:
# https://github.com/pypa/pip/issues/6164
# If we don't do this, pip will fail to install the dependencies.
# We need to import the global variables in order to
# use them in the following imports.
from . import global_vars

import logging
import os
import requests
import sys
import zipfile

from . import global_vars

def download_file(url, filename):
    # NOTE the stream=True parameter
    r = requests.get(
