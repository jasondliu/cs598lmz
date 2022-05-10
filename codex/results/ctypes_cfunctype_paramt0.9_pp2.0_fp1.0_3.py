import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

testlib = ctypes.CDLL('./libtestlib.so')
testlib.add.argtypes = (ctypes.c_int, ctypes.c_int)
testlib.add.restype = ctypes.c_int

def call_add(x, y):
    return testlib.add(x, y)

CALLBACK_TYPE = FUNTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class Obj(object):

    def __init__(self):
        self.obj_id = testlib.create()
        self.__callback = CALLBACK_TYPE(self.callback)

    def __del__(self):
        testlib.release(self.obj_id)

    def callback(self, a, b):
        print a + b
        return a + b

    def set_callback(self):
        print self.__callback
        testlib.set_callback(self.obj_id,
