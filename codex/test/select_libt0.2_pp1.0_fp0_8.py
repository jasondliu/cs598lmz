import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import constants
from . import exceptions
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_sock_lock = threading.Lock()
_g_sock_list = []

