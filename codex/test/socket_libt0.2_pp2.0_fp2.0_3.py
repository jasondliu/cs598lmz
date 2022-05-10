import socket
import sys
import threading
import time
import traceback

import pytest

from . import util
from . import test_base
from . import test_net
from . import test_node
from . import test_wallet
from . import test_zmq

# Hack to import from parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib import config
from lib import exceptions
from lib import log
from lib import util

from server import server

logger = log.get_logger()

# TODO: Test that the server is actually running

def test_server_startup_shutdown():
    """
    Test that the server starts and stops cleanly.
    """
    # Start the server
    server.start()
    # Stop the server
    server.stop()

def test_server_startup_shutdown_with_config():
    """
    Test that the server starts and stops cleanly with a configuration file.
    """
    # Start the server
