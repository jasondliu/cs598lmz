import ctypes
# Test ctypes.CFUNCTYPE(None)
def callback():
    print("callback()")

CALLBACK = ctypes.CFUNCTYPE(None)

try:
    CALLBACK()
except TypeError:
    print("TypeError: callback() takes no arguments (1 given)")
