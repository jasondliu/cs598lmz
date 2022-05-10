import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import traceback
import urllib2
import zipfile

from . import common
from . import config
from . import constants
from . import database
from . import db_utils
from . import errors
from . import file_utils
from . import logger
from . import metadata
from . import plugins
from . import utils
from . import version

# The following are used for the 'sort' parameter in get_files_by_metadata
# and get_files_by_metadata_bulk.
SORT_BY_NAME = 'name'
SORT_BY_DATE = 'date'
SORT_BY_SIZE = 'size'

# The following are used for the 'sort_dir' parameter in get_files_by_metadata
# and get_files_by_metadata_bulk.
SORT_ASCENDING = 'asc'
SORT_DESCENDING = 'desc'

# The following are used for the 'type' parameter in get_files_by_metadata
# and get_
