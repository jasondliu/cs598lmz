import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from . import logger
from . import utils

#
# Define some constants
#

# The default directory to look for the configuration file in
DEFAULT_CONFIG_DIR = "~/.config/pwman3"

# The default name of the configuration file
DEFAULT_CONFIG_FILE = "config"

# The default directory to look for the database file in
DEFAULT_DB_DIR = "~/.config/pwman3"

# The default name of the database file
DEFAULT_DB_FILE = "db"

# The default password length
DEFAULT_PASSWORD_LENGTH = 20

# The default number of passwords to generate
DEFAULT_PASSWORD_COUNT = 1

# The default number of seconds to wait for a key press
DEFAULT_KEYPRESS_TIMEOUT = 5

# The default number of seconds to wait before clearing the screen
DEFAULT_SCREEN_CLEAR_TIMEOUT = 5

# The default number of
