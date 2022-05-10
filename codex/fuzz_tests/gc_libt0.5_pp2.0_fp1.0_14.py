import gc, weakref

class WeakRef(object):
    def __init__(self, item):
        self.item = weakref.ref(item)
    def __call__(self):
        return self.item()
    def __getattr__(self, name):
        return getattr(self.item(), name)
    def __setattr__(self, name, value):
        if name == 'item':
            self.__dict__[name] = weakref.ref(value)
        else:
            setattr(self.item(), name, value)

class WeakRefDict(dict):
    def __getitem__(self, item):
        return WeakRef(dict.__getitem__(self, item))
    def __setitem__(self, item, value):
        dict.__setitem__(self, item, value)
        dict.__setitem__(self, item, value)
    def __delitem__(self, item):
        dict.__delitem__(self, item)

class WeakRefList(list):
    def __getitem__(self
