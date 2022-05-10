import weakref
# Test weakref.ref() on this class.
class A:
    def foo(self):
        pass
class Proxy(object):

    def __init__(self, obj):
        self._wrapped = obj

    __getattr__ = lambda self, n: getattr(self._wrapped, n)

    # The extra method exists to prevent the Proxy from
    # matching the exact type of the wrapped object.

    def unwrap(self):
        return self._wrapped
# This test should be successful; the proxy should make itself weakly
# referential.
