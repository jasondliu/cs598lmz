import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from . import config
from . import constants
from . import errors
from . import util
from . import version
from . import xar_subset
from . import xar_util
from . import xar_xml
from . import xcode_util
from . import xip_util
from . import xip_verify

from . import xcode_util
from . import xip_util
from . import xip_verify

#
# Constants
#

# The maximum number of times to retry the extraction of a .xip file.
_MAX_XIP_EXTRACT_RETRIES = 3

# The number of seconds to wait between retries of the extraction of a .xip
# file.
_XIP_EXTRACT_RETRY_WAIT = 5

# The maximum number of times to retry the extraction of a .xar file.
_MAX_XAR_EXTRACT_RETRIES = 3

# The
