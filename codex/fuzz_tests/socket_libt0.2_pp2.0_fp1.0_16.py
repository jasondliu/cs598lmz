import socket
import sys
import threading
import time
import traceback

import pytest

import stomp
from stomp.exception import ConnectFailedException
from stomp.exception import NotConnectedException
from stomp.exception import StompException
from stomp.exception import StompFrameError
from stomp.exception import StompProtocolError
from stomp.exception import StompSessionError
from stomp.exception import StompTimeoutException
from stomp.exception import UnsupportedProtocolError
from stomp.listener import TestListener
from stomp.test.testutils import *


class Test12Connect(object):

    def test_connect_v12(self):
        conn = stomp.Connection12(get_default_host())
        conn.set_listener('', TestListener())
        conn.start()
        conn.connect(get_default_user(), get_default_password(), wait=True)
        conn.disconnect(receipt=None)

    def test_connect_v12_with_ssl(self):
        conn = stomp.Connection12(get_default_host(), use_ssl
