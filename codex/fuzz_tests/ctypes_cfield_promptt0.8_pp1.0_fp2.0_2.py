import ctypes
# Test ctypes.CField implementation

_fld = ('z', ctypes.c_byte, 1), ('a', ctypes.c_byte, 7), ('b', ctypes.c_byte, 8), ('c', ctypes.c_short, 16), ('d', ctypes.c_int, 32), ('e', ctypes.c_longlong, 64)

class TestStructure(ctypes.Structure):
    _fields_ = _fld

class TestUnion(ctypes.Union):
    _fields_ = _fld

class Test(object):
    def test(self, name, instance, exp_size, exp_alignment, *expct):
        exp_alignment = getattr(instance, '_alignment_', exp_alignment)
        size = ctypes.sizeof(instance)
        alignment = ctypes.alignment(instance)
        if name:
            print('\n%s' % (name,))
            print(' size: %d, should be %d' % (size, exp_size))
            print(' alignment: %d, should be %d' %
