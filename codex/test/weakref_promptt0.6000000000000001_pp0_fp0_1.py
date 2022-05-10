import weakref
# Test weakref.ref(arg, callback)
import gc

class MyClass:
    pass

def callback(x):
    print('callback(', x, ')')

def callback2(x):
    print('callback2(', x, ')')

def callback3(x):
    print('callback3(', x, ')')

def callback4(x):
    print('callback4(', x, ')')

def callback5(x):
    print('callback5(', x, ')')

def callback6(x):
    print('callback6(', x, ')')

def callback7(x):
    print('callback7(', x, ')')

def callback8(x):
    print('callback8(', x, ')')

def callback9(x):
    print('callback9(', x, ')')

def callback10(x):
    print('callback10(', x, ')')

def callback11(x):
    print('callback11(', x, ')')

