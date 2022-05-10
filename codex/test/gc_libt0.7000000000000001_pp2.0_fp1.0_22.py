import gc, weakref, time

class Evil(object):
    def __init__(self, name):
        self.name = name

class EvilRef(weakref.ref):
    def __init__(self, obj, callback=None):
        self.__name = obj.name
        super(EvilRef, self).__init__(obj, callback)

