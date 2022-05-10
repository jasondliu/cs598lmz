import _struct
import threading
import time
import unittest

from pymodbus.constants import Defaults
from pymodbus.transaction import ModbusSocketFramer, ModbusRtuFramer
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.compat import IS_PYTHON3

# --------------------------------------------------------------------------- #
# Fixture
# --------------------------------------------------------------------------- #
class ModbusFramerTest(unittest.TestCase):
    '''
    This is the unittest for the pymodbus.transaction module
    '''

    def setUp(self):
        ''' Initializes the test environment '''
        self.framer = ModbusSocketFramer(None)

    def tearDown(self):
        ''' Cleans up the test environment '''
        del self.framer

    def testPayload(self):
        ''' Test basic payload building '''
        payload  = struct.pack(">HHH", 0x0001, 0x0003, 0x0004)
        payload += struct
