import gc, weakref

class Object(object):
    def __init__(self):
        self.name = "object"
    def __repr__(self):
        return self.name

class Invoker(Object):
    def __init__(self, obj):
        self.name = "invoker"
        self.obj = obj
