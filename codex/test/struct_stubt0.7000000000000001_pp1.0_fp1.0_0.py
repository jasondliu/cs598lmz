from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.pack(0)

# struct.pack(c, 0) is b'\x00'
# struct.pack(c, 1) is b'\x01'
# struct.pack(c, -1) is b'\xff'
# struct.pack(c, 2**31) is b'\x80\x00\x00\x00'
# struct.pack(c, -2**31) is b'\x80\x00\x00\x01'
# struct.pack(c, 2**31-1) is b'\xff\xff\xff\x7f'
# struct.pack(c, -2**31+1) is b'\xff\xff\xff\x7f'

# struct.unpack(c, b'\x00') is (0,)
# struct.unpack(c, b'\x01') is (1,)
# struct.unpack(c, b'\xff') is (-1,)
# struct.unpack(c,
