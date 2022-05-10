import weakref
# Test weakref.ref()
import sys
import gc

class MyObject(object):
    def myMethod(self):
        pass

class MyClass(object):
    def __init__(self):
        self.o = MyObject()
