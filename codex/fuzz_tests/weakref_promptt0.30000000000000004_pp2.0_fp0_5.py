import weakref
# Test weakref.ref(obj, callback)

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(ref):
    print 'callback(', ref, ')'

def callback2(ref):
    print 'callback2(', ref, ')'

def callback3(ref):
    print 'callback3(', ref, ')'

def callback4(ref):
    print 'callback4(', ref, ')'

def callback5(ref):
    print 'callback5(', ref, ')'

def callback6(ref):
    print 'callback6(', ref, ')'

def callback7(ref):
    print 'callback7(', ref, ')'

def callback8(ref):
    print 'callback8(', ref, ')'

def callback9(ref):
    print 'callback9(', ref, ')'

def callback10(ref):
    print 'callback10(', ref, ')'

def callback11
