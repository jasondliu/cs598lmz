import weakref
# Test weakref.ref(obj)
with TestSection('weakref.ref(obj)'):
    class Obj(object):
        pass
    obj = Obj()
    ref = weakref.ref(obj)
    assert ref() is obj
    del obj
    assert ref() is None

# Test weakref.ref(obj, callback)
with TestSection('weakref.ref(obj, callback)'):
    class Obj(object):
        pass
    obj = Obj()
    def callback(obj):
        callback.called = True
    callback.called = False
    ref = weakref.ref(obj, callback)
    assert ref() is obj
    del obj
    assert ref() is None
    assert callback.called

# Test weakref.WeakValueDictionary
with TestSection('weakref.WeakValueDictionary'):
    class Obj(object):
        pass
    obj = Obj()
    wvd = weakref.WeakValueDictionary()
    wvd['key'] = obj
    assert wvd['key'] is obj
    del obj
    assert 'key' not in wvd

# Test weak
