import weakref
# Test weakref.ref

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

def test_callback(r):
    print('test_callback(', r, ')')

def test_callback2(r):
    print('test_callback2(', r, ')')

def test_callback3(r):
    print('test_callback3(', r, ')')

def test_callback4(r):
    print('test_callback4(', r, ')')

def test_callback5(r):
    print('test_callback5(', r, ')')

def test_callback6(r):
    print('test_callback6(', r, ')')

def test_callback7(r):
    print('test_callback7(', r, ')')

def test_callback8(r):
    print('test_
