import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class test_library(object):
    def __init__(self, name):
        self.name = name
        self.loaded = False

    def load(self):
        lib = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), self.name))
        self.test1 = FUNTYPE(lib.test1)
        self.test2 = FUNTYPE(lib.test2)
        self.test3 = FUNTYPE(lib.test3)
        self.test4 = FUNTYPE(lib.test4)
        self.test5 = FUNTYPE(lib.test5)
        self.test6 = FUNTYPE(lib.test6)
        self.test7 = FUNTYPE(lib.test7)
        self.test8 = FUNTYPE(lib.test8)
        self.test9 = FUNTYPE(lib.test9)
        self.test10 = FUNTYPE(lib.test10)
        self.test11 = FUNTYPE(lib.test11)
        self.test12 = FUNTYPE(lib.test
