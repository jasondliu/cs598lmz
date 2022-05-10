import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class Test:

    def __init__(self):
        self.counter = 0

    def __call__(self):
        tmp = self.counter
        self.counter += 1
        return tmp

test = Test()

test_cfunc = FUNTYPE(test)

test_cfunc()  # 0
test_cfunc()  # 1
test_cfunc()  # 2
</code>

