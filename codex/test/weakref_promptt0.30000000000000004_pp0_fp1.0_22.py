import weakref
# Test weakref.ref(obj, callback)

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

def callback2(r):
    print('callback2(', r, ')')

def callback3(r):
    print('callback3(', r, ')')

def callback4(r):
    print('callback4(', r, ')')

def callback5(r):
    print('callback5(', r, ')')

def callback6(r):
    print('callback6(', r, ')')

def callback7(r):
    print('callback7(', r, ')')

def callback8(r):
    print('callback8(', r, ')')

def callback9(r):
    print('callback9(', r, ')')

