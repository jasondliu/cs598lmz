import weakref
# Test weakref.ref() with callbacks

def callback(ref):
    print 'callback(', ref, ')'

def callback_ex(unused, ref):
    print 'callback_ex(', unused, ref, ')'

def callback_kw(**kwds):
    print 'callback_kw(', kwds, ')'

class MyObject:
    def __init__(self):
        self.callback_args = None
        self.callback_kwds = None
    def callback(self, ref):
        print 'MyObject.callback(', self, ref, ')'
        self.callback_args = (ref,)
    def callback_ex(self, ref):
        print 'MyObject.callback_ex(', self, ref, ')'
        self.callback_args = (ref,)
    def callback_kw(self, **kwds):
        print 'MyObject.callback_kw(', self, kwds, ')'
        self.callback_kwds = kwds

def test_callback(test):
    o = MyObject()
    ref = weakref.ref(
