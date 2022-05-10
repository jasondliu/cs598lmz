import ctypes
ctypes.cast(0, ctypes.py_object)
assert ctypes.cast(0, ctypes.py_object) is None

# XXX An application should be able to create CObject instances directly,
# XXX but I can't find a way to do that with ctypes.  There is a CData class
# XXX but there doesn't seem to be away to specialize that to type PyObject.
# XXX So, until I find a way to do that, this test has to omit the test
# s, p = run_python("""if 1:
#     import ctypes
#     print(ctypes.cast(0, ctypes.py_object))
# """)
# assert s == 0, "subprocess failed"
# assert p.strip() == 'None', p

print("testing rpython side of module")

pypy = py.magic.autopath().dirpath().dirpath().dirpath().dirpath()

import sys
from pypy.module.cpyext.test.test_cpyext import AppTestCpythonExtensionBase

def test_args_error():
    class TestApp
