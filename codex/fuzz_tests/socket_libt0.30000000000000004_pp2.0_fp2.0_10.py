import socket
import sys
import threading
import time
import traceback

from . import config
from . import db
from . import log
from . import util
from . import version

# A global variable used to indicate that the server should be shut down.
_shutdown = False

# A global variable used to indicate that the server should be restarted.
_restart = False

# A global variable used to indicate that the server should be reloaded.
_reload = False

# A global variable used to indicate that the server should be reloaded.
_reload_config = False

# A global variable used to indicate that the server should be reloaded.
_reload_db = False

# A global variable used to indicate that the server should be reloaded.
_reload_log = False

# A global variable used to indicate that the server should be reloaded.
_reload_util = False

# A global variable used to indicate that the server should be reloaded.
_reload_version = False

# A global variable used to indicate that the server should be reloaded.
_reload
