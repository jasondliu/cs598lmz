import gc, weakref

class C:
    def __init__(self, name, referent):
        self.name = name
        self.ref = weakref.ref(referent)
    def __repr__(self):
        return 'C({})'.format(self.name)

