import weakref
# Test weakref.ref(dict)

class DictRef(object):
    def __init__(self, dict):
        self.dict = dict

    def __call__(self):
        return self.dict

class C(object):
    def __init__(self):
        self.d = {1:1}
        self.r = weakref.ref(self.d, DictRef(self.d))

    def test_method(self):
        assert self.r() is self.d

def test_method():
    obj = C()
    obj.test_method()
    obj.d = None
    rgc.collect()
    assert obj.r() is None

# Test weakref.ref(dict) with a callback that raises an exception

def callback_method(d):
    raise Exception("Exception in callback")

def test_callback_method():
    obj = C()
    obj.r = weakref.ref(obj.d, callback_method)
    obj.d = None
    rgc.collect()
    raises(Exception, "obj.r()")
