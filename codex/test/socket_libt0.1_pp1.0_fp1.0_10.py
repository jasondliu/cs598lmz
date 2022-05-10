import socket
import sys
import threading
import time
import traceback

import pytest

from . import util
from . import test_util
from . import test_pb2
from . import test_pb2_grpc
from .test_server import start_test_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_REQUEST = b'\x00\x00\x00' b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'
_RESPONSE = b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'
_REQUEST_SLOW = b'\x00\x00\x00' b'\x00\x00\x00\x00' b'\x00\x00\x00\x01'
_RESPONSE_SLOW = b'\x00\x00\x00\x01' b'\x00\x00\x00\x00'
