from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4si')
print(s.format)
print(s.size)
print(s.pack("ddd", 3.24, 1.4, 2.3))
print(s.pack("ddd", 3.24, 1.4, 2.3).hex())
print(s.unpack("ddd","\x88\x13\x9a\x99\x0c\x00\x00\x00\x90\x85\xeb\x51"))


class Struct(Struct):
    def __init__(self, fmt, endian="=", verbose=False) -> None:
        self.__format__ = _fmt(fmt, endian)
        self.__fmt__, self.__fmt_verbose__ = fmt, fmt
        self.__endian__ = endian
        self.__verbose__ = verbose
        self.__size__ = self.size
        super().__init__(self.__format__)

