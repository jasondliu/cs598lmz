import ctypes
# Test ctypes.CFUNCTYPE(None)

import _ctypes_test

def callback():
    print("callback")

CALLBACK = ctypes.CFUNCTYPE(None)

_ctypes_test.set_callback(CALLBACK(callback))
# raises TypeError: Don't know how to convert parameter 1
_ctypes_test.set_callback(CALLBACK)
</code>
Also I want to test a simple python code with a ctypes callback:
<code>import ctypes
# Callback

CALLBACK = ctypes.CFUNCTYPE(None)

def callback():
    print("callback")

CALLBACK(callback)()
</code>
I got following error:
<code>TypeError: 'NoneType' object is not callable
</code>
I'm using Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) on Windows.
All the other test functions( such as ctypes.c_int, ctypes.POINTER) are working. Why does callback function does not work
