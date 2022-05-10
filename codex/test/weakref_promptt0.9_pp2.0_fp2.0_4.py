import weakref
# Test weakref.ref (methods, callbacks)

class C(object):

    def __init__(self, callback=None):
        self.callback = callback

    def __call__(self):
        if self.callback is not None:
            self.callback()

class A(object):

    def __init__(self):
        self.refs = []

    def add(self, c):
        x = weakref.ref(c, self.callback)
        self.refs.append(x)

    def callback(self, wr):
        l = self.refs
        l.remove(wr)

    def __del__(self):
        # don't call back into self.callback
        self.refs = []

    def n(self, n):
        for i in range(n):
            l = self.refs
            l.remove(l[0])


def callback(wr):
    g.append(wr())

