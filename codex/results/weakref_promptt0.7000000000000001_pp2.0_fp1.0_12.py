import weakref
# Test weakref.ref() with callbacks.
import _weakref

# Test weakref.ref() with callbacks.


class MyRef(weakref.ref):

    def __call__(self):
        return self.__weakref__ is not None

class Foo:

    def __init__(self, callback):
        self.callback = callback

    def __call__(self, *args):
        self.callback(*args)

    def __del__(self):
        self.callback(self)


class MyRef2(_weakref.ref):

    def __call__(self):
        return self.__weakref__ is not None


class Foo2:

    def __init__(self, callback):
        self.callback = callback

    def __call__(self, *args):
        self.callback(*args)

    def __del__(self):
        self.callback(self)


class MyRef2a(weakref.ref):

    def __call__(self):
        return self.__weakref__ is not None

class Foo2a:

    def __init
