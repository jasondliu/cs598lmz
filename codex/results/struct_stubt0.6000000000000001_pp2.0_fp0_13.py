from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)

print unpack(pack((1, 'xy', 2.3)))
</code>

