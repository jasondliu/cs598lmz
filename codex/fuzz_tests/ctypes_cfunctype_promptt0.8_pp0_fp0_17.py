import ctypes
# Test ctypes.CFUNCTYPE

def test_c_function_pointer():
    import _ctypes
    import sys

    if sys.platform == 'win32':
        prefix = '@12'
    else:
        prefix = '_'
    def _test(name, argtypes, restype, errcheck, prot):
        proto = _ctypes.CFUNCTYPE(restype, *argtypes)
        cfunc = proto((prefix + name, _ctypes.RTLD_GLOBAL), prot)
        cfunc.errcheck = errcheck
        return cfunc

    def check_int_result(result, func, args):
        if result == 0:
            raise SystemError
        else:
            return result

    def check_c_string_result(result, func, args):
        if result:
            return ctypes.string_at(result)
        else:
            # no string
            return None

    def check_arg(value):
        if not isinstance(value, ctypes.c_char_p):
            raise ArgumentError(value)

    _strlen = _test
