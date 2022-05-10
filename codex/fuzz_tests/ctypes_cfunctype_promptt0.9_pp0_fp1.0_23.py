import ctypes
# Test ctypes.CFUNCTYPE()
# Test tp_call flag.
# Test only defaults arguments.

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)
try:
    dll.writestring('\0')
except WindowsError, details:
    # It is okay if the process was killed by the debuggee -
    # but not if it is something else.
    if details.winerror != 299:
        raise

def check_tp_call(argtypes, proc, func, retval, args):
    #
    # create the argtypes and proto based on the func argtypes and return
    # value.
    p = ctypes.CFUNCTYPE(func.restype, *argtypes)(proc)
    # CFUNCTYPE stores the address of the function in p
    assert p._func is not None
    assert p._flags_ and ISFUNCFLAG
    assert p.__call__ is not None
    assert p(1, 2) == retval
    p = p.__call__
    assert p is not None
    assert p
