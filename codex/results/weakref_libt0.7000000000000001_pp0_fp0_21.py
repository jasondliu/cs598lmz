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


def serial_for_url(url, timeout=1, write_timeout=1, **kwargs):
    """
    Helper function to open an arbitrary serial URL.
    For example::

        >>> s = serial_for_url('loop://', timeout=1)
        >>> s.write(b'hello')
        5
        >>> s.read(5)
        b'hello'

    ``url`` is a URL that describes the serial connection to use.
    Currently supported schemes are:

    - ``'loop://'`` - connects to a local pty; data written to the serial port
      is immediately read from it
    - ``'
