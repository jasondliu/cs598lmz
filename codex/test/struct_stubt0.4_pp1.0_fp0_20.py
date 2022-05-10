from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>hhl')
s.unpack_from(b'\x00\x01\x00\x02\x00\x00\x00\x03', 0)

# 可以用一个类来模拟其他类的实例。为此，你需要定义一个特殊的__call__()方法，
# 就像下面这样：
import socket

class LazyConnection:
    def __init__(self, address, family=socket.AF_INET, type=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
