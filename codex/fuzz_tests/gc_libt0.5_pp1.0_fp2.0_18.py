import gc, weakref
from collections import defaultdict

class gc_hook(object):
    def __init__(self, callback):
        self.callback = callback
        self.wr = weakref.ref(self, self.callback)

    def __del__(self):
        self.callback()

def create_gc_hook(callback):
    return gc_hook(callback)

class WeakMethod(object):
    def __init__(self, func, parent):
        self.func = func
        self.parent = weakref.ref(parent)
    
    def __call__(self, *args, **kwargs):
        return self.func(self.parent(), *args, **kwargs)

class WeakMethodProxy(object):
    def __init__(self, parent):
        self.parent = weakref.ref(parent)
    
    def __getattr__(self, name):
        return WeakMethod(getattr(self.parent(), name), self.parent())

class WeakMethodProxyDict(object):
    def __init__(self, parent):
        self
