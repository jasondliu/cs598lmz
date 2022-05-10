import mmap
import os
import re
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# -----------------------------------------------------------------------------
# Globals

# The name of the file that contains the current version of the application.
VERSION_FILE = 'version.txt'

# The name of the file that contains the current version of the application.
VERSION_FILE_DEV = 'version_dev.txt'

# The name of the file that contains the current version of the application.
VERSION_FILE_DEV_BETA = 'version_dev_beta.txt'

# The name of the file that contains the current version of the application.
VERSION_FILE_DEV_RC = 'version_dev_rc.txt'

# The name of the file that contains the current version of the application.
VERSION_FILE_DEV_ALPHA = 'version_dev_alpha.txt'

# The name of the file that contains the current version of the application.
VERSION_FILE_DEV_SNAPSHOT = 'version_dev_snapshot.txt'

# The
