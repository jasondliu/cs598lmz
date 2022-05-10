from _struct import Struct
s = Struct.__new__(Struct)
try:
    s.__init__('I 2s f', byteorder='big')
except TypeError:
    print('SKIP')
    raise SystemExit

buf = s.pack(3, b'ab', 2.5)
print(s.unpack(buf))
