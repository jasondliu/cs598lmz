import select
import socket
import sys
import time
import threading
import traceback

import numpy as np

from . import constants
from . import exceptions
from . import packet
from . import util
from . import v4l2

class Device(object):
    def __init__(self, device_path):
        self._device_path = device_path
        self._device_file = open(device_path, 'rb')
        self._device_file_no = self._device_file.fileno()
        self._device_file_name = self._device_file.name
        self._device_file_lock = threading.Lock()

        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket_lock = threading.Lock()

        self._socket_thread = None
        self._socket_thread_lock = threading.Lock()

        self._socket_thread_stop_event = threading.Event()
        self._socket_thread_stop_event_lock = threading.Lock()

        self._socket
