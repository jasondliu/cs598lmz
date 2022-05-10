import mmap
import os
import re
import sys
import time
import traceback

from typing import Iterable, List, Optional, Union

from . import __version__, config, language, log, utils

# The maximum number of times we'll attempt to retry a command.
MAX_RETRIES = 3

# The number of seconds we'll wait between retries.
RETRY_WAIT_TIME = 0.5

# The number of seconds we'll wait for the language server to respond to a
# request.
REQUEST_TIMEOUT = 45

# The number of seconds we'll wait for the language server to start.
START_TIMEOUT = 60

# The number of seconds we'll wait for the language server to stop.
STOP_TIMEOUT = 5

# The number of seconds we'll wait for the language server to send a
# notification.
NOTIFICATION_TIMEOUT = 0.5

# The number of seconds we'll wait for the language server to send a
# request.
REQUEST_TIMEOUT = 0.5

# The number of seconds we'll wait for the language server to
