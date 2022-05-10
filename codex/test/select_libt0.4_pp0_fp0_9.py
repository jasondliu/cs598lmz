import select
import socket
import sys
import time

import pytest

from umodbus.client.serial import rtu
from umodbus.client.serial.rtu import RtuClient
from umodbus.client.serial.rtu_rt import RtuClient as RtuClientRT
from umodbus.client.serial.rtu_io import RtuClient as RtuClientIO
from umodbus.client.serial.rtu_select import RtuClient as RtuClientSelect
from umodbus.client.serial.rtu_epoll import RtuClient as RtuClientEpoll
from umodbus.client.serial.rtu_asyncio import RtuClient as RtuClientAsyncIO
from umodbus.client.serial.rtu_asyncio_aio import RtuClient as RtuClientAsyncIOAsync
from umodbus.client.serial.rtu_asyncio_async import RtuClient as RtuClientAsyncIOAsyncIO
