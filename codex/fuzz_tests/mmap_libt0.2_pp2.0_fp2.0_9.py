import mmap
import os
import re
import sys
import time

from . import config
from . import utils
from . import version
from . import xdg

# TODO:
# - Add a --no-color option.
# - Add a --no-pager option.
# - Add a --no-progress option.
# - Add a --no-status option.
# - Add a --no-title option.
# - Add a --no-truncate option.
# - Add a --no-unicode option.
# - Add a --no-wrap option.
# - Add a --no-wrap-search option.
# - Add a --no-wrap-scroll option.
# - Add a --no-wrap-titles option.
# - Add a --no-wrap-view option.
# - Add a --no-xterm-titles option.
# - Add a --pager option.
# - Add a --pager-end option.
# - Add a --pager-start option.
# - Add a --pager-start-size option.
# - Add a
