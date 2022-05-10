import weakref
# Test weakref.ref() and weakref.proxy()
#
#   - weakref.ref(o) returns a weak reference to o.
#     When the object is no longer used, the reference object is deleted,
#     and subsequent calls to the weak reference object raise a ReferenceError.
#     The weak reference object can be called and will return the original object.
#
#   - weakref.proxy(o, callback=None) returns a weak proxy to o.
#     The proxy is callable and implements the same interface
#     as the object, even if the object does not have a suitable __call__ method.
#     When the object is no longer used, the reference is deleted,
#     and subsequent calls to the proxy object raise a ReferenceError.
#     The callback function is called with a reference to the proxy,
#     and can be used to perform additional clean-up actions.
class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("(Deleting {})".format(self))

