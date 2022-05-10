from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# Subclassing Struct
class MyStruct(Struct):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class Point(Structure):
    _fields_ = [('x', c_int),
                ('y', c_int)]

class Address(Structure):
    _fields_ = [('hostname', c_char_p),
                ('port', c_int)]

class PolyHeader(Structure):
    _fields_ = [('length', c_int),
                ('width', c_int),
                ('height', c_int)]

class Polygon(Structure):
    _fields_ = [('header', PolyHeader),
                ('points', POINTER(Point))]

