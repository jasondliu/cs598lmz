import weakref
# Test weakref.ref(instance_method):
class Foo(object):
    def __init__(self, callback):
        self.callback = callback

