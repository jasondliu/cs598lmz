import mmap
import os
import re
import sys
import time
import traceback

from . import config
from . import utils
from . import version
from . import xdg

# TODO:
# - Add a way to specify a list of files to be ignored.
# - Add a way to specify a list of directories to be ignored.
# - Add a way to specify a list of files to be included.
# - Add a way to specify a list of directories to be included.
# - Add a way to specify a list of files to be excluded.
# - Add a way to specify a list of directories to be excluded.
# - Add a way to specify a list of files to be included.
# - Add a way to specify a list of directories to be included.
# - Add a way to specify a list of files to be excluded.
# - Add a way to specify a list of directories to be excluded.
# - Add a way to specify a list of files to be included.
# - Add a way to specify a list of directories to be included.
# - Add a way to specify a list of files to be excluded.

