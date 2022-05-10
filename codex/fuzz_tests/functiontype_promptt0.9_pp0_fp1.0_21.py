import types
# Test types.FunctionType and types.MethodType
import test_types
import unittest
import weakref

# These three classes are used in testing class methods.
class Class():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.__class__.__name__ + '(' + repr(self.value) + ')'

    def method(self, arg):
        return self.value * arg

    def method2(self, arg):
        return self.method(arg)

class Class2(Class):
    def method(self, arg):
        return self.value + arg

def function(self, arg):
    return self.value // arg

def check_lossage(func):
    if hasattr(func, '__self__'):
        raise AssertionError("automatically determined __self__ does not match __get__(None, type)")
    if hasattr(func, '__func__'):
        raise AssertionError("automatically determined __func__ does not match __get__(None
