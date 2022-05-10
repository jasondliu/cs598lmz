import gc, weakref

class C:
    def __init__(self, name, referent):
        self.name = name
        self.ref = weakref.ref(referent)
    def __repr__(self):
        return 'C({})'.format(self.name)

o = C('o')

o.a = C('a', o)
o.b = C('b', o)

print(o.a.ref())
print(o.b.ref())

print(gc.get_referents(o))
print(gc.get_referents(o)[1])
print(gc.get_r
