import weakref
# Test weakref.ref() for the "callable" attribute and the __call__() method.
import sys

class CallableRefTestClass:
    def __init__(self, ignore):
        self.called = False
    def __call__(self):
        self.called = True
    def called_get(self):
        return self.called
    def called_set(self, value):
        self.called = value
    called = property(called_get, called_set)

def callable_ref_test():
    obj = CallableRefTestClass(None)
    ref = weakref.ref(obj)
    print(ref.__call__() is obj)
    print(ref()) is obj
    print(ref.called)
    ref.called = False
    ref()
    print(ref.called)

callable_ref_test()
