import weakref
# Test weakref.ref(func)

class KeyedRef(object):
    def __init__(self, obj, key):
        self.key = key
        self.obj = weakref.ref(obj)

    def __call__(self):
        return self.obj()[self.key]

    def __hash__(self):
        return hash((self.obj, self.key))

    def __eq__(self, other):
        return self.obj() is other.obj() and self.key == other.key

class C(object):
    def __init__(self):
        self.__dict__['x'] = 1
        self.__dict__['y'] = 2

c = C()
w1 = KeyedRef(c, 'x')
w2 = KeyedRef(c, 'y')
w3 = KeyedRef(c, 'x')
