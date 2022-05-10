import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

import pkg_resources
import yaml

from . import __version__
from . import config
from . import constants
from . import log
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_AIO_CONFIG_FILE = 'aio.yml'
_AIO_CONFIG_FILE_FULL_PATH = os.path.join(constants.PATH_AIO_CONFIG, _AIO_CONFIG_FILE)
_AIO_CONFIG_FILE_BACKUP = '{}.bak'.format(_AIO_CONFIG_FILE_FULL_PATH)
_AIO_CONFIG_FILE_BACKUP_TMP = '{}.tmp'.format(_AIO_CONFIG_FILE_FULL_PATH)

_AIO_CONFIG_FILE_BACKUP_DIR = os.path.join(constants.PATH_A
