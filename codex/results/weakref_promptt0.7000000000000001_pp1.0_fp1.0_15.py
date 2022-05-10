import weakref
# Test weakref.ref() for a builtin function
import __builtin__
import sys
import pickle

class MyClass:
    def __init__(self, name):
        self.name = name

def func1():
    pass

def func2(a):
    pass

def func3(a, *b):
    pass

def func4(a, **b):
    pass

def func5(a, *b, **c):
    pass

def func6(a, b=2, c=3):
    pass

def func7(a, b=2, c=3, *d):
    pass

def func8(a, b=2, c=3, **d):
    pass

def func9(a, b=2, c=3, *d, **e):
    pass

def func10(a, b):
    pass

def func11(a, b, *c):
    pass

def func12(a, b, **c):
    pass

def func13(a, b, *c, **
