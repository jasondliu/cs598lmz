import mmap
import os
import re
import sys
import time

from . import __version__
from . import config
from . import utils

log = logging.getLogger(__name__)

# This is the default location of the file containing the list of
# packages that are to be ignored.
DEFAULT_IGNORE_FILE = '/etc/portage/package.mask'

# This is the default location of the file containing the list of
# packages that are to be unmasked.
DEFAULT_UNMASK_FILE = '/etc/portage/package.unmask'

# This is the default location of the file containing the list of
# packages that are to be unmasked.
DEFAULT_KEYWORDS_FILE = '/etc/portage/package.accept_keywords'

# This is the default location of the file containing the list of
# packages that are to be unmasked.
DEFAULT_LICENSE_FILE = '/etc/portage/package.license'

# This is the default location of the file containing the list of
# packages that are to be unmasked
