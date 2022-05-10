import weakref
# Test weakref.ref(self) for a weak reference to self
# in a method of a class instance.
# This is to test weakref.proxy(self) in proxy_method.

class C(object):
    def __init__(self):
        self.a = 1
        self.ref = weakref.ref(self)
        self.proxy = weakref.proxy(self)
    def f(self):
        return self.a + 1

    def f_ref(self):
        return self.a + 1 + self.ref().a

    def f_proxy(self):
        return self.a + 1 + self.proxy.a

    def f_proxy_ref(self):
        return self.a + 1 + self.proxy.a + self.ref().a

    def f_proxy_ref_ref(self):
        return self.a + 1 + self.proxy.a + self.ref().a + self.ref().a

    def f_proxy_ref_ref_ref(self):
        return self.a + 1 + self.proxy.a + self.ref().a + self.
