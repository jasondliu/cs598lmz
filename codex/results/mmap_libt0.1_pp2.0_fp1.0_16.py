import mmap
import os
import re
import sys
import time

from . import config
from . import util
from . import xdg

# TODO:
# - add a --force option to override the check for existing files
# - add a --dry-run option to print the commands that would be run
# - add a --verbose option to print the commands that are run
# - add a --quiet option to suppress all output
# - add a --no-color option to suppress color output
# - add a --no-progress option to suppress progress output
# - add a --no-progress-bar option to suppress progress bar output
# - add a --no-progress-dots option to suppress progress dots output
# - add a --no-progress-spinner option to suppress progress spinner output
# - add a --no-progress-percent option to suppress progress percent output
# - add a --no-progress-eta option to suppress progress eta output
# - add a --no-progress-speed option to suppress progress speed output
# - add a --no-progress-size option to suppress progress size output
# - add a --no
