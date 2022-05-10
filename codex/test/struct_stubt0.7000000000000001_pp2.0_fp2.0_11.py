from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b')
s.unpack_from(b'\x00\x01\x02', 1)

def c(p):
    return s.unpack_from(p.bin, p.offset)

class GameData(BinaryObject):
    def __init__(self):
        self.name = c(PString())

import sys
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
sys.stdout.buffer.write(b'\x00\x01\x02')
