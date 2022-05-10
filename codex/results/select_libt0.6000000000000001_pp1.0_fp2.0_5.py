import select
import socket
import threading
import time
import unittest

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Defaults
from pymodbus.exceptions import ConnectionException, ModbusException
from pymodbus.factory import ClientDecoder
from pymodbus.pdu import ModbusExceptions
from pymodbus.register_read_message import ReadHoldingRegistersRequest
from pymodbus.utilities import checkCRC

from .async_server import start_async_server, stop_async_server
from .mockserver import start_test_server, stop_test_server


class ModbusTcpClientTest(unittest.TestCase):
    '''
    This is the unittest for the pymodbus.client.sync module
    '''

    @classmethod
    def setUpClass(cls):
        cls.client = start_test_server()

    @classmethod
    def tearDownClass(cls):
        stop_test_server()

    def setUp(self):

