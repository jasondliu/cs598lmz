import gc, weakref, time

class Evil(object):
    def __init__(self, name):
        self.name = name

class EvilRef(weakref.ref):
    def __init__(self, obj, callback=None):
        self.__name = obj.name
        super(EvilRef, self).__init__(obj, callback)

    def __call__(self):
        print self.__name, "was dereferenced"
        return super(EvilRef, self).__call__()

    def __eq__(self, other):
        return self() == other()

    def __ne__(self, other):
        return self() != other()

    def __nonzero__(self):
        return self() is not None

    def __hash__(self):
        return hash(self())

    def __repr__(self):
        return repr(self())

if __name__ == '__main__':
    bag = set()
    while len(bag) &lt; 4:
        bag.add(EvilRef(Evil("evil %d" % len(
