from _struct import Struct
s = Struct.__new__(Struct)
s.s = '<h'
s.pack(1)
'\x00\x01'
bytes(s.pack(1))
b'\x00\x01'
b = bytes(s.pack(1))
b
b'\x00\x01'
b[0]
0
len(b)
2
b[0] = 0xFF
b
b'\xff\x01'


# stdlib
from ctypes import Structure, c_int
class S(Structure):_fields_ = [('a', c_int)]
S
<class '__main__.S'>
S.a
<Field type=c_long, ofs=0: a>
S.a.__get__
<method-wrapper '__get__' of c_long_Array_3 object at 0x7f744e512368>
S.a.__get__(None, None)
<cparam 'P' (0x7f744e512368)>
S.a.__get__(None, S)
<attribute 'a
