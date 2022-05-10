import gc, weakref

"""
The purpose of this module is to provide a class that allows an object to be
created only once, and then to return the same object over and over again.
This is useful to ensure that the object is a singleton, as well as to
provide a convenient mechanism for referencing the object.
"""

class Singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance

def SingletonDecorator(aClass):
    return Singleton(aClass)

class WeakSingleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance

