import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class MyClass(object):
    def __init__(self):
        self.callback = FUNTYPE(self.my_callback)

    def my_callback(self):
        print "Callback called"

mc = MyClass()
mc.callback()
</code>

