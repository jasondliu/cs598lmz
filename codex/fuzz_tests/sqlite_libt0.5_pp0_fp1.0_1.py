import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import os
import sys
import signal

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/var/log/pwdsafe.log',
                    filemode='a')

# This is a simple python wrapper for the pwsafe library. It is intended to
# provide a simple interface to the library.

# The pwsafe library is a python wrapper for the pwsafe C library. It is
# intended to provide a simple interface to the C library.

# The pwsafe C library is a wrapper for the pwsafe.org library. It is intended
# to provide a simple interface to the pwsafe.org library.

# The pwsafe.org library is intended to provide a simple, secure, portable,
# and extensible API for handling encrypted password databases.

# The pwdsafe application is a simple python script that provides a cli for
# the pwsafe library.


class PwsafeError(Exception):
    """
