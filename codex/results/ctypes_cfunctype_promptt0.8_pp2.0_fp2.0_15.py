import ctypes
# Test ctypes.CFUNCTYPE callback
def callback(name, val):
    print('"%s"=%s' % (name, val))

# Create an instance of the callback
callback.__class__ = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_ulonglong)

# Pass instance as the callback
lib.test_array(callback)
</code>

