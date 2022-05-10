import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object({})

def test_cpython_issue_14470():
    # Issue 14470: Don't crash if globals are a resized dict.
    def f():
        from types import ModuleType
        m = ModuleType('test')
        m.__dict__.update({'blah':1})
        return m

    r = f()
    r.__dict__

def test_cpython_issue_7695():
    # Issue 7695: Don't crash when a function is called with a
    # too-small stack frame (if the function references a local
    # variable of a function with a large stack frame).
    import sys
    import dis
    import types
    import marshal
    import struct

    if sys.flags.optimize > 0:
        py.test.skip("with -O optimization, the bug doesn't happen")

    def calcsize(string):
        return struct.calcsize(string)

    def generate_function(codesize):
        # Generate a function that will use codesize bytes when executed.
        def
