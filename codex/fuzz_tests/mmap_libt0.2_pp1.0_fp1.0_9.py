import mmap
import os
import re
import sys
import time

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# The following is a list of all the possible options that can be passed to
# the command line.
#
# The format is:
#
#   (long option, short option, description, default value)
#
# The default value is only used if the option is not specified in the
# configuration file.
#
# If the default value is None, then the option is required.
#
# If the short option is None, then the option is not available on the
# command line.
#
# If the description is None, then the option is not available in the
# configuration file.
#
# If the long option is None, then the option is not available at all.
#
# The description is used in the usage message and in the configuration file
# comments.
#
# The long option is used on the command line.
#
# The short option is used on the command line.
#
# The default value is
