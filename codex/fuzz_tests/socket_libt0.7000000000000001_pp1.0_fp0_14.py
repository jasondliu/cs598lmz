import socket
import time
import thread
import threading
import sys
import Queue
import unittest
from subprocess import Popen, PIPE

# local import
import vncdotool.client
from vncdotool.client import VNCDoToolConnectionClosed
from vncdotool.vnc import VNCConnectionClosed, VNCProtocolError
from vncdotool.rfb import RFBError
from vncdotool import rfb
from vncdotool import vnc
from vncdotool import rfb
from vncdotool.vncdotool import VNCDoTool


class TestVNCDoTool(unittest.TestCase):
    """ 
        Integration test for vncdotool. 
    """

    def setUp(self):
        self.host = 'localhost'
        self.port = 5900
        self.password = 'test'
        self.p = None
        self.vncserver_proc = None
        self.vncserver_proc = Popen(['vncserver', '-
