import gc, weakref


class Impl(object):
    def __init__(self, source):
        self.source = source
        self.data = []
        self.rref = weakref.ref(self, self.clean)
    def append(self, value):
        self.data.append(value)
        self.rref = weakref.ref(self, self.clean)
