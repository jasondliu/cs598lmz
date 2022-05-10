import ctypes
# Test ctypes.CFUNCTYPE
#
# The main test is that this code compiles

def foo():
    pass

def bar(a,b,c=3,d=4):
    pass

def baz(a,b=2,c=3):
    pass

def qux(a,b,*c):
    pass

def quux(a,*b):
    pass

class cls(object):
    def foo(self):
        pass

    def bar(self,a,b,c=3,d=4):
        pass

    def baz(self,a,b=2,c=3):
        pass

    def qux(self,a,b,*c):
        pass

    def quux(self,a,*b):
        pass

def raise_(err):
    raise err

