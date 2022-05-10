import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import sys
import os
import re
import shutil
import traceback

from . import config

_log = logging.getLogger(__name__)


def _get_os_system_metrics():
    """Return OS-specific system metrics."""
    if sys.platform == "win32":
        # Windows
        SM_CXSCREEN = 0
        SM_CYSCREEN = 1
        SM_CXVSCROLL = 2
        SM_CYHSCROLL = 3
        SM_CYCAPTION = 4
        SM_CXBORDER = 5
        SM_CYBORDER = 6
        SM_CXDLGFRAME = 7
        SM_CYDLGFRAME = 8
        SM_CYVTHUMB = 9
        SM_CXHTHUMB = 10
        SM_CXICON = 11
        SM_CYICON = 12
        SM_CXCURSOR = 13
        SM_CYCURSOR = 14
        SM
