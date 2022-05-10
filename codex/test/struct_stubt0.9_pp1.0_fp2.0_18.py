from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'bB'
s.size = s.calcsize()

def s_unpack(data):
    "Unpack from the front of the data buffer"
    return s.unpack(data)

def s_pack(data, *values):
    "Pack values and append to the end of the data buffer"
    return s.pack(_data, *values)
