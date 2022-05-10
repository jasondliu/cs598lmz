import socket
import sys
import time
import os
import subprocess
import threading
import signal
import logging
import json
import re

from . import utils
from . import config
from . import log
from . import constants
from . import exceptions
from . import __version__
from . import __author__
from . import __email__
from . import __url__
from . import __license__
from . import __copyright__

logger = logging.getLogger(__name__)

# TODO:
# - add a way to specify the port
# - add a way to specify the interface
# - add a way to specify the hostname
# - add a way to specify the protocol
# - add a way to specify the timeout
# - add a way to specify the retries
# - add a way to specify the delay
# - add a way to specify the debug
# - add a way to specify the verbose
# - add a way to specify the quiet
# - add a way to specify the log file
# - add a way to specify the log level
# - add a way to specify the log
