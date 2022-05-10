import ctypes
# Test ctypes.CFUNCTYPE in a class
class Test(object):
    def __init__(self):
        self.foo = ctypes.CFUNCTYPE(None)
        if self.foo is None:
            raise Exception("self.foo is None")

Test()
