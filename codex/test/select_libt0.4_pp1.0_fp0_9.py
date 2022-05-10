import select
import socket
import sys
import time

from . import base
from . import exceptions
from . import utils
from . import version
from . import __version__ as pymodbus_version

#---------------------------------------------------------------------------#
# Logging
#---------------------------------------------------------------------------#
import logging
_logger = logging.getLogger(__name__)

#---------------------------------------------------------------------------#
# Constants
#---------------------------------------------------------------------------#
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 502

#---------------------------------------------------------------------------#
