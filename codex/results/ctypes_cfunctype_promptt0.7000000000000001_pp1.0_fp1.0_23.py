import ctypes
# Test ctypes.CFUNCTYPE vs ctypes.WINFUNCTYPE on Windows.

from ctypes import *

def test_CFUNCTYPE():
    # This works.
    CallBackProc = CFUNCTYPE(c_int, c_int, c_int, c_int)
    print(CallBackProc)
    print(CallBackProc(5,5,5,5))

def test_WINFUNCTYPE():
    # This doesn't work.
    CallBackProc = WINFUNCTYPE(c_int, c_int, c_int, c_int)
    print(CallBackProc)
    print(CallBackProc(5,5,5,5))


if __name__ == "__main__":
    test_CFUNCTYPE()
    test_WINFUNCTYPE()
</code>
And here is the output:
<code>&lt;class 'ctypes.WINFUNCTYPE'&gt;
&lt;ctypes.WINFUNCTYPE object at 0x00000000029D6268&gt;

