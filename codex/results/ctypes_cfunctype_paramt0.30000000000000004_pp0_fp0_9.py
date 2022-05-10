import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Test(object):
    def __init__(self):
        self.callback = FUNTYPE(self.callback_func)

    def callback_func(self, i):
        print "callback_func called with %d" % i
        return i

t = Test()
t.callback(1)
</code>

