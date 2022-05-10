import ctypes

class S(ctypes.Structure):
    x = 32
    y = 16
    _fields_ = [('a', ctypes.c_uint8, x),
                ('b', ctypes.c_uint8, y),
                ('c', ctypes.c_uint8, (x - y))]

if __name__ == '__main__':
    s = S()
    assert ctypes.sizeof(s) == 4
    assert ctypes.sizeof(s._fields_[0][1]) == 4
    assert ctypes.sizeof(s._fields_[1][1]) == 2
    assert ctypes.sizeof(s._fields_[2][1]) == 1
    assert ctypes.sizeof(s._fields_[0][1]._type_) == 4
    assert ctypes.sizeof(s._fields_[1][1]._type_) == 2
    assert ctypes.sizeof(s._fields_[2][1]._type_) == 1
    assert s._fields_[0][1]._type_._length_ == 32
    assert s._fields_[1][1].
