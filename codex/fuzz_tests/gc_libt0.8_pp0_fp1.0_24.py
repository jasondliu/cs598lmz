import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

class D(C):
    pass

# create a reference cycle
c = C('c')
d = D('d')

c.r = weakref.ref(d)
d.r = weakref.ref(c)

# these objects will be collected
o = C('o')

# but c and d will not be collected until this reference is deleted
dlist = weakref.WeakValueDictionary()
dlist['c'] = c
dlist['d'] = d
dlist['o'] = o

print 'before gc:', dlist.keys()
print 'before gc:', [x() for x in dlist.values()]
del o
print 'after o is deleted:', dlist.keys()
print 'after o is deleted:', [x() for x in dlist.values()]

gc.collect()

print 'after g
