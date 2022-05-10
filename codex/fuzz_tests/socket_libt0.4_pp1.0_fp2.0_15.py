import socket
import struct
import sys
import threading
import time

from . import common
from . import constants
from . import exceptions
from . import packet
from . import utils

_LOGGER = logging.getLogger(__name__)


class WemoLink:
    """Class to represent a WeMo Link."""

    def __init__(self, host, port=constants.PORT):
        """Initialize the WeMo Link."""
        self.host = host
        self.port = port
        self.name = None
        self.serialnumber = None
        self.mac = None
        self.model_name = None
        self.model_number = None
        self.firmware_version = None
        self.friendly_name = None
        self.manufacturer = None
        self.manufacturer_url = None
        self.model_description = None
        self.model_url = None
        self.upc = None
        self.bulbs = []
        self.bulb_count = 0
        self.bulb_max = 0
        self.bul
