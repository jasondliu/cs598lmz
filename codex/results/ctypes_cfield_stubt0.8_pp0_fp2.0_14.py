import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    import sys
    if sys.argv[1:] == ['cfield_set']:
        CFieldTest().test_field_setting()
    if sys.argv[1:] == ['cfield_get']:
        CFieldTest().test_field_getting()
    if sys.argv[1:] == ['ctype_instance']:
        CTypeTest().test_instance()
    if sys.argv[1:] == ['ctype_call']:
        CTypeTest().test_call()

if __name__ == '__main__':
    main()
