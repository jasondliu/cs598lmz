from _struct import Struct
s = Struct.__new__(Struct)
print(s)


# Example 2
class Struct:
    def __init__(self, format, *args):
        self.format = format
        self.size = Struct.calcsize(format)
        self.data = Struct.pack(format, *args)

    def pack(self, format, *args):
        pass

    def unpack(self, data):
        pass

    def unpack_from(self, data, offset=0):
        pass

    def calcsize(self):
        pass


