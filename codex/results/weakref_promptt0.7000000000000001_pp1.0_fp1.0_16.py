import weakref
# Test weakref.ref(classinstance)
# WeakRefTest.py
import weakref
class C(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print 'I am dead'

c = C('name')
cref = weakref.ref(c)
print cref().name
del c
print cref()
# Test weakref.ref callbacks
# WeakRefCallBackTest.py
import weakref
class C(object):
    def __init__(self, name):
        self.name = name
        self.called = False
    def __del__(self):
        self.called = True

c = C('name')
cref = weakref.ref(c, lambda x: setattr(x, 'called', True))
print cref().name
del c
print cref()
print cref().called
# Test weakref.finalize
# WeakRefFinalizeTest.py
import weakref
class C(object):
    def __init__(self, value):
        self.value = value
