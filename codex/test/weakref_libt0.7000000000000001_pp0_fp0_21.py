import weakref
# from .zmodem import Zmodem, ZmodemCancelledException
import io
import logging
import platform
import serial
import serial.tools.list_ports
import sys
import threading
import time
import weakref
from .zmodem import Zmodem, ZmodemCancelledException
import logging
logger = logging.getLogger(__name__)


__all__ = ['Serial', 'serial_for_url']


