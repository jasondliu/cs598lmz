import select
import signal
import sys
import time
import traceback

import pytest

import pymodbus.exceptions
import pymodbus.factory
import pymodbus.pdu
import pymodbus.transaction
import pymodbus.utilities


#---------------------------------------------------------------------------#
# Fixture
#---------------------------------------------------------------------------#
@pytest.fixture(scope="module")
def modbus_tcp_server(request, tcp_server):
    """
    This fixture creates a modbus server that can handle tcp requests
    """
    server = pymodbus.factory.ServerDecoder(tcp_server)
    server.add_slave(1)
    server.add_block('0', pymodbus.coils.Bits(0, [1, 1, 1, 1, 1, 1, 1, 1]))
    server.add_block('1', pymodbus.discrete.Bits(0, [1, 1, 1, 1, 1, 1, 1, 1]))
