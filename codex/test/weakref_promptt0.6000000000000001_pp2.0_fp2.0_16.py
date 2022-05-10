import weakref
# Test weakref.ref callbacks

# Check that a callback is called when a weak reference goes out of scope
# and another callback is called when the callback is deleted

class Foo:
    pass

def get_ref():
    f = Foo()
    return weakref.ref(f, callback)

def callback(ref):
    global called
    called = True
    ref.cb = None

def get_cb():
    global called
    called = False
    ref = get_ref()
    ref.cb = weakref.ref(ref, delete_cb)
    return ref

def delete_cb(ref):
    global called
    called = True

def test_callbacks():
    ref = get_cb()
    del ref
    assert called, 'Callback not called when weak reference goes out of scope'
    called = False
    ref = get_cb()
    del ref.cb
    assert called, 'Callback not called when callback is deleted'

test_callbacks()
