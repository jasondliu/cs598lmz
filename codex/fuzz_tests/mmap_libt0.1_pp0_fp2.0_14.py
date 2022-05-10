import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# The following are used to determine the default value of the
# --config-dir option.

# The default configuration directory.
DEFAULT_CONFIG_DIR = '~/.config/pipx'

# The default configuration directory for Windows.
DEFAULT_CONFIG_DIR_WINDOWS = '~/AppData/Roaming/pipx'

# The default configuration directory for MacOS.
DEFAULT_CONFIG_DIR_MACOS = '~/Library/Application Support/pipx'

# The default configuration directory for Linux.
DEFAULT_CONFIG_DIR_LINUX = '~/.config/pipx'

# The default configuration directory for other platforms.
DEFAULT_CONFIG_DIR_OTHER = '~/.config/pipx'

# The default configuration directory for Windows.
DEFAULT_DATA_DIR_WINDOWS = '~/AppData/Local/pipx'

