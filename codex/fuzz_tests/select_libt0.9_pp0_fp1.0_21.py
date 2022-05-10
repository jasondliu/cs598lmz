import select
import socket
from inspect import signature

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.pdu import ExceptionResponse
from pymodbus.pdu import ModbusRequest, ModbusResponse
from pymodbus.pdu import ReadHoldingRegistersRequest, ReadHoldingRegistersResponse
from pymodbus.pdu import ReadDiscreteInputsRequest, ReadDiscreteInputsResponse
from pymodbus.pdu import ReadCoilsRequest, ReadCoilsResponse
from pymodbus.pdu import WriteMultipleCoilsRequest, WriteMultipleCoilsResponse
from pymodbus.pdu import WriteMultipleRegistersRequest, WriteMultipleRegistersResponse

from pandas import DataFrame
from functools import partial, update_wrapper
from typing import Callable, List, Tuple, Union, Optional
from multiprocessing import Process, Queue, cpu_count

import logging
log = logging.getLogger(__name__)


def default_name_func(host, port):
    return "PyModbus({0}:{1})".format(host, port
