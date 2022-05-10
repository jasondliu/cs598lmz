import _struct

_pack_ = 1

class B(Structure):
    _fields_ = [("a", c_uint32), ("b", c_uint32)]

class C(Structure):
    _fields_ = [("b", B), ("c", B)]

class D(Structure):
    _fields_ = [("c", C), ("d", c_uint32)]

class E(Structure):
    _fields_ = [("d", D), ("e", c_uint32)]

class F(Structure):
    _fields_ = [("e", E), ("f", c_uint32)]

class G(Structure):
    _fields_ = [("f", F), ("g", c_uint32)]

class H(Structure):
    _fields_ = [("g", G), ("h", c_uint32)]

class I(Structure):
    _fields_ = [("h", H), ("i", c_uint32)]

class J(Structure):
    _fields_ = [("i", I), ("j", c
