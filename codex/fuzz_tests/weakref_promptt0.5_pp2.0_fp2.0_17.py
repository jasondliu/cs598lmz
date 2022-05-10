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
    def __del__(self):
        print "MyClass.__del__"

def callback(r):
    print "callback", r

print "Testing weakref.ref()"
o = MyObject()
r = weakref.ref(o)
print "o:", o
print "r:", r
print "r():", r()
print "o is r():", o is r()
print "o is r() is r():", o is r() is r()
print "o is r():", o is r()
print "o == r():", o == r()
print "o == r() == r():", o == r() == r()
print "o == r():", o == r()
o = None
print "o is r():", o is r()
print

print "Testing weakref.ref(callback)"
o = MyObject
