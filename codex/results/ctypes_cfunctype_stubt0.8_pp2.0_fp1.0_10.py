import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 13

class C:
    pass

old_b=C.__bases__
C.__bases__=(fun,)
print C.__bases__[0]()
C.__bases__=old_b

#try:
#    print C.__bases__[0]()
#except Exception, e:
#    print e

class MyInt(object):
    def __init__(self, x):
        self.x=x
        def __int__(self):
            return self.x

print int(MyInt(10))

#from ctypes import py_object, sizeof, POINTER, c_byte, pointer, c_long
#funptr = ctypes.CFUNCTYPE(py_object, py_object)
#def my_callback(x):
#    print "hello", x
#callback = funptr(my_callback)

a = []
print a.__sizeof__()
