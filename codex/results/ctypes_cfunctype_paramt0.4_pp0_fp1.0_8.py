import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class MyClass(object):
    def __init__(self):
        self.callback = FUNTYPE(self.my_callback)

    def my_callback(self, arg):
        print 'called back with', arg
        return 0

c = MyClass()
c.callback(1)
</code>

