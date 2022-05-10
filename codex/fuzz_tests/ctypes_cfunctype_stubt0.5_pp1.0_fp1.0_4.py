import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class MyObject(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

def test_fun():
    fun()

def test_object():
    obj = MyObject("hello")
    obj.getName()

def test_iter():
    l = [1, 2, 3]
    for i in l:
        pass
    for i in l:
        pass

def test_list():
    l = [1, 2, 3]
    l[0]

def test_tuple():
    t = (1, 2, 3)
    t[0]

def test_dict():
    d = {1: 2, 2: 3}
    d[1]

def test_set():
    s = {1, 2, 3}
    s.add(4)

def test_str():
    s = "hello"
    s[0]

def test_int():
    i = 1
    i + 1
