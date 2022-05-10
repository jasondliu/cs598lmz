from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.size
class MyStruct(Struct):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class MyStruct(Structure):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class MyStruct(Structure):
    _pack_ = 2
    _fields_ = [('x', c_int),
                ('y', c_int)]

class Point(Structure):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class PolyHeader(Structure):
    _fields_ = [('len', c_int),
                ('type', c_int),
                ('closed', c_int)]

class PolyHeader(Structure):
    _fields_ = [('len', c_int),
                ('type', c_int),
                ('closed', c_int)]
