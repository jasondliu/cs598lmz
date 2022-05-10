import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import config
from . import utils
from . import version

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------

# The maximum number of times to retry a request.
MAX_RETRIES = 5

# The maximum number of times to retry a request that failed with a
# recoverable error.
MAX_RETRIES_RECOVERABLE = 3

# The maximum number of times to retry a request that failed with a
# recoverable error.
MAX_RETRIES_RECOVERABLE = 3

# The maximum number of times to retry a request that failed with a
# recoverable error.
MAX_RETRIES_RECOVERABLE = 3

# The maximum number of times to retry a request that failed with a
# recoverable error.
MAX_RETRIES_RECOVERABLE = 3

# The maximum number of times to retry a request that failed with a

