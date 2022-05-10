import mmap
import os
import re
import subprocess
import sys
import tempfile
import time

from . import config
from . import util
from . import version
from . import vcs
from . import xdg

# The name of the file that contains the version of the last build.
LAST_BUILD_VERSION_FILE = 'last_build_version'

# The name of the file that contains the version of the last build that was
# successful.
LAST_SUCCESSFUL_BUILD_VERSION_FILE = 'last_successful_build_version'

# The name of the file that contains the version of the last build that was
# successful and was not a no-op.
LAST_SUCCESSFUL_NON_NOOP_BUILD_VERSION_FILE = \
    'last_successful_non_noop_build_version'

# The name of the file that contains the version of the last build that was
# successful and was not a no-op and was not a dry run.
LAST_SUCCESSFUL_NON_NOOP_NON_DRY_
