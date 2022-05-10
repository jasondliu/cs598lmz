import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(object):
    def __init__(self):
        self.__dict__['y'] = S()
        self.__dict__['y'].x = 5
        self.__dict__['y'].x = 6

a = A()
