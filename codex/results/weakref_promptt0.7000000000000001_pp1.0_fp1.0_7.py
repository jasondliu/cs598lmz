import weakref
# Test weakref.ref(obj), where obj is a list, dict, tuple, or set.
# We expect the weak reference to trigger on del lst[:] (which replaces
# the list), but not on del lst[i].

class List(list):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.wr = weakref.ref(self, self.callback)

    def callback(self, arg):
        print('callback({})'.format(arg))
        print('    self:', self)
        print('    type(self):', type(self))
        print('    len(self):', len(self))
        print('    self[0]:', self[0])
        raise TypeError(self)

class Dict(dict):
    # Like List, but for dicts.

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.wr = weakref.ref(self, self.callback)

    def callback(self, arg):

