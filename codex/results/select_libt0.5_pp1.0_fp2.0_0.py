import select
import socket
import sys
import threading
import time

import mock
from six.moves import queue

from grpc import _common
from grpc.framework.foundation import logging_pool
from grpc.framework.interfaces.links import links
from tests.unit import test_common

_REQUEST_MESSAGE = b'\x00\x00\x00'
_RESPONSE_MESSAGE = b'\x00\x00\x00\x00'


class _TestLink(links.Link):

  def __init__(self, request_message, response_message, response_delay):
    self._request_message = request_message
    self._response_message = response_message
    self._response_delay = response_delay

  def consume(self, request_iterator):
    for request in request_iterator:
      yield self._response_message
      time.sleep(self._response_delay)

  def terminate(self):
    pass


class _TestHandler(object):

  def __init__(self, request_message, response
