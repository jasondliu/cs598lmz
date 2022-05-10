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
# Client Factories
#---------------------------------------------------------------------------#
class ModbusClientFactory(object):
    """
    Factory for creating modbus clients.

    This factory will create the appropriate modbus client based on the
    supplied arguments.  The arguments can be a port number, host name,
    or a tuple of host and port number.

    :param host: The host to connect to (default localhost)
    :param port: The modbus port to connect to (default 502)
    :param framer: The modbus framer to use (default ModbusRtuFramer)
    :param source_address: The TCP source
