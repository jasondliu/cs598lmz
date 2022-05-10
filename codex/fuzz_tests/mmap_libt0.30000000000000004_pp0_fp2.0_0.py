import mmap
import os
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

from .log import getLogger

logger = getLogger(__name__)

#
# The following is a list of all the files that we need to
# be able to access on the system.  The list is in the form
# of a dictionary, where the key is the name of the file,
# and the value is a tuple of the form (type, description).
#
# The type is one of:
#
#   - "file" - a regular file
#   - "dir"  - a directory
#   - "link" - a symbolic link
#
# The description is a short string that describes the file
# in question.  This is used in the error message if the file
# is not found.
#
# The list is used in two places:
#
#   - to check that all the files exist before we start
#     the daemon
#
#   - to check that
