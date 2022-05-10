import ctypes
# Test ctypes.CFUNCTYPE callback
def callback(name, val):
    print('"%s"=%s' % (name, val))

# Create an instance of the callback
