import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(None)
def callback():
    print('called callback')

