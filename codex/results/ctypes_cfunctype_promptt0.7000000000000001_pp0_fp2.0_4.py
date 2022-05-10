import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_double)

class A():
    def __init__(self):
        print("Init")
        self.my_callback = ctypes.CFUNCTYPE(None, ctypes.c_double)(self.callback)

    def callback(self, data):
        print("Callback:" + str(data))

a = A()
</code>

