import mmap
import os
import re
import sys
import time

from . import config
from . import util

# TODO:
# - Add a --force option to override the existing file.
# - Add a --dry-run option to not actually write the file.
# - Add a --verbose option to print out the file as it's being written.
# - Add a --show-diff option to show the diff between the existing file and the
#   new file.
# - Add a --show-diff-only option to only show the diff between the existing
#   file and the new file.
# - Add a --show-diff-full option to show the full diff between the existing
#   file and the new file.
# - Add a --show-diff-full-only option to only show the full diff between the
#   existing file and the new file.
# - Add a --show-diff-full-color option to show the full diff between the
#   existing file and the new file in color.
# - Add a --show-diff-full-color-only option to only show the full diff between
#  
