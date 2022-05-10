import weakref
# Test weakref.ref(classinstance)
# WeakRefTest.py
import weakref
class C(object):
    def __init__(self, name):
        self.name = name

