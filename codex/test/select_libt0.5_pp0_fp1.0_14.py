import select
import sys
import threading
import time

import pytest

import grpc
from grpc._cython import cygrpc
from grpc.framework.interfaces.face import face
from tests.unit.framework.common import test_constants
from tests.unit.framework.interfaces.face import test_utilities

_REQUEST = b'\x00\x00\x00'
_RESPONSE = b'\x00\x00\x00\x00'
_REQUEST_SLICE = memoryview(_REQUEST)
_RESPONSE_SLICE = memoryview(_RESPONSE)
_REQUEST_SLICE_SIZE = len(_REQUEST_SLICE)
_RESPONSE_SLICE_SIZE = len(_RESPONSE_SLICE)
_HALF_CLOSE = True
_TAG = b'\x00'
_CALL_METADATA = ((b'key', b'value'),)
_STATUS = grpc.StatusCode.OK
_STATUS_DETAILS = 'details'
