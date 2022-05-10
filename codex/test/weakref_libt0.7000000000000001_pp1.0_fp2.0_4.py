import weakref

class MethodWrapper(object):
    "method adaptor"
    def __init__(self, obj, method):
        self.obj = obj
        self.method = method

    def __call__(self, *args, **kwds):
        self.method(self.obj, *args, **kwds)

class Event(object):
    "event"
    def __init__(self):
        self.handlers = []

    def __iadd__(self, handler):
        self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.handlers:
            handler(*args, **keywargs)

