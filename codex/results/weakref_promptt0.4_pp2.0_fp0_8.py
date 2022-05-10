import weakref
# Test weakref.ref(object, callback)
#
# This test is not exhaustive, but it does test the following:
#   - callback is called when the referent is deleted
#   - callback is not called when the weak reference is deleted
#   - callback is not called when the referent is garbage collected
#   - callback is not called when the weak reference is garbage collected

class Object(object):
    pass

class Ref(weakref.ref):
    def __init__(self, ob, callback):
        self.callback = callback
        super(Ref, self).__init__(ob, self.callback)

def test_callback(ob, callback):
    ref = Ref(ob, callback)
    del ob
    assert ref() is None
    assert callback.called
    callback.called = False
    del ref
    assert not callback.called

class Callback(object):
    def __init__(self):
        self.called = False
    def __call__(self, ref):
        self.called = True

def test_callback_class():
    ob = Object()
    callback = Call
