import socket
from time import time
import sys
import asyncio
import asyncio_redis
from crc16 import crc16xmodem


def log(*args, **kwargs):
    print(*args, **kwargs)


class YzBinaryReader:

    def __init__(self, data):
        self.stream = io.BytesIO(data)

    def read_string(self, count):
        ret = self.stream.read(count)
        ret = ret.decode()
        ret = ret.replace('\x00', '')
        return ret

    def read_byte(self):
        return int.from_bytes(self.stream.read(1), byteorder='big', signed=False)

    def read_bytes(self, count):
        return self.stream.read(count)

    def read_int16(self):
        return int.from_bytes(self.stream.read(2), byteorder='big', signed=True)

