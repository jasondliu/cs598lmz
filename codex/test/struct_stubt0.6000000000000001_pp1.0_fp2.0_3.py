from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes(4+2+4), 4)

s.unpack_from(_, 0)

import socket
import array
import struct

L2TP_HEADER_FORMAT = '!BBH'
L2TP_HEADER_SIZE = struct.calcsize(L2TP_HEADER_FORMAT)

class L2TP(object):
    def __init__(self, source, destination, tid, cid):
        self.source = source
        self.destination = destination
        self.tid = tid
        self.cid = cid

    def pack(self):
        return struct.pack(L2TP_HEADER_FORMAT, self.source, self.destination, self.tid, self.cid)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
