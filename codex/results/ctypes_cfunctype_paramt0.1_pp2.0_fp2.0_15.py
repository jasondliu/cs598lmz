import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class MyClass(object):
    def __init__(self):
        self.callback = FUNTYPE(self.callback)

    def callback(self, arg):
        print "callback called with arg:", arg
        return 0

my_class = MyClass()
my_class.callback(42)
</code>

