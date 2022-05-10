import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    s.x = 0
    t = S(1)

    # ctypes.Structure
    assert(isinstance(S, type))
    assert(issubclass(S, ctypes.Structure))

    assert(S._fields_ == [('x', ctypes.c_int)])
    assert(S._pack_ == 1)
    assert(S.__dict__ == {
        '_fields_': [('x', ctypes.c_int)],
        '_pack_': 1,
        'x': <CField type at 0x10b844a08>
    })

    # ctypes.CField
    assert(isinstance(s.x, ctypes.CField))
    assert(isinstance(getattr(s, 'x'), ctypes.c_int))
    assert(s.x == 0)

    # ctypes.Structure.__new__
    assert(isinstance(s, S))
    assert(issubclass(type(s), S))
    assert(S.__
