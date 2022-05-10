import mmap
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
from collections import namedtuple
from io import StringIO
from pathlib import Path
from typing import List, Optional, Tuple, Union

import click
import git
from click import ClickException, confirm

from .. import __version__, config, utils
from ..config import get_config, save_config
from ..constants import (
    DEFAULT_CONFIG_FILE,
    DEFAULT_CONFIG_FILE_NAME,
    DEFAULT_CONFIG_FILE_PATH,
    DEFAULT_EXCLUDE_LIST,
    DEFAULT_EXCLUDE_LIST_PATH,
    DEFAULT_TEMPLATE_PATH,
    DEFAULT_TEMPLATE_PATH_NAME,
    DEFAULT_TEMPLATE_PATH_PATH,
    DEFAULT_TEMPLATE_PATH_URL,
    DEFAULT_TEMPLATE_PATH_URL_NAME,
    DEFAULT_TEMPLATE_PATH_URL_PATH,
    DEFAULT_TEM
