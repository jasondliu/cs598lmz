from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<BHI")
# Note that this just unpacks the binary data. What is missing?
s

class MyStruct():
    def __init__(self, fmt="<BHI"):
        self.struct = Struct.__new__(Struct)
        self.struct.__init__(fmt)
    def unpack(self, data, offset=0):
        self.data = self.struct.unpack(data[offset:offset+self.struct.size])
        return vars(self)
v = MyStruct()
v.unpack(b'\x01\x02\x03\x04\x05')
v.data

class Msg():
    def __init__(self, fmt="<BHI"):
        self.head = MyStruct(fmt)
    def unpack(self, data, offset=0):
        self.head.unpack(data, offset)
        return vars(self)

msg = Msg()
msg.unpack(b'\x01\x02\x03\x04
