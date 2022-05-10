import weakref
# Test weakref.ref(obj, callback)
import sys

class C:
    pass

callback_called = False

def callback(wr):
    global callback_called
    callback_called = True

c = C()
wr = weakref.ref(c, callback)
del c
assert callback_called

# Test weakref.ref(obj, callback) with an object that is not weak-referenceable
# by default.

class D:
    def __del__(self):
        pass

callback_called = False

def callback(wr):
    global callback_called
    callback_called = True

d = D()
wr = weakref.ref(d, callback)
del d
assert callback_called

# Test weakref.ref(obj, callback) with an object that is not weak-referenceable
# by default, and has a __del__ method that raises an exception.

class E:
    def __del__(self):
        raise Exception

callback_called = False

def callback(wr):
    global callback_called
    callback_called = True

e
