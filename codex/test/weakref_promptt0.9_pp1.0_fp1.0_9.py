import weakref
# Test weakref.ref()
class TestRef():
    pass

obj = TestRef()
ref = weakref.ref(obj)
