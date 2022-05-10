import weakref
# Test weakref.ref(obj, callback) to make sure callback is called when
# the object is garbage collected.

class Test(object):
    pass

class Callback(object):
    def __init__(self):
        self.called = False

    def __call__(self, ref):
        self.called = True

def callback(obj, other):
    obj.called = True
    if other is not None:
        other.called = True

class MyCallbackClass(object):
    def __init__(self, obj, other):
        self.obj = obj
        self.other = other
    def __call__(self, ref):
        callback(self.obj, self.other)

def callback_subtype(obj, other):
    obj.called = True
    if other is not None:
        other.called = True

class MyCallbackSubtype(MyCallbackClass):
    def __call__(self, ref):
        callback_subtype(self.obj, self.other)

class MyCallbackSubtype2(MyCallbackClass):
    pass

