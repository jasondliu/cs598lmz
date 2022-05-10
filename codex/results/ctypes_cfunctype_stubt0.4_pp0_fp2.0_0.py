import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
def fun2():
    return 2
fun.__name__ = 'fun'
fun2.__name__ = 'fun2'
fun2.__module__ = '__main__'

class A(object):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return self.value

class C(object):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return self.value

class D(object):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return self.value

class E(object):
    def __init__(self, value):
        self.value = value
