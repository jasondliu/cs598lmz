import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import re
import logging

from . import __version__
from . import __author__
from . import __email__
from . import __license__
from . import __url__
from . import __description__

logger = logging.getLogger(__name__)

# The following code is based on
# https://github.com/jamescasbon/py-applescript/blob/master/applescript/__init__.py

# TODO: Add support for the following:
# - kAEGetData
# - kAESetData
# - kAESendMessage
# - kAECreateDesc
# - kAECreateAppleEvent
# - kAECreateList
# - kAECreateRecord
# - kAEDisposeDesc
# - kAEPutParamDesc
# - kAEPutParamPtr
# - kAEPutParamPtr
# - kAEPutParamPtr
# - kAEPutParamPtr
# - kAEPutParamPtr
# - kA
