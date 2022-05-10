import weakref
# Test weakref.ref callback argument:


class Foo(object):

    def __init__(self):
        self.__callbacks = {}
        self.__refcallbacks = {}
        self.__alive = True

    def __del__(self):
        self.__alive = False

    def callback(self, key):
        if self.__alive:
            self.__callbacks[key] = 1

    def iscallback(self, key):
        return self.__callbacks.get(key)

    def refcallback(self, key, ref):
        if self.__alive:
            self.__refcallbacks[key] = 1

    def isrefcallback(self, key):
        return self.__refcallbacks.get(key)


def callback(self, key):
    if self.__alive:
        self.__callbacks[key] = 1


def refcallback(self, key, ref):
    if self.__alive:
        self.__refcallbacks[key] = 1


