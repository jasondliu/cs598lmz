import weakref
# Test weakref.ref


class C(object):
    pass


o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
del o
gc.collect()
print(r)
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = C()
d['a'] = o
print(d['a'] is o)
del o
gc.collect()
try:
    print(d['a'])
except KeyError:
    print("KeyError")
# Test weakref.WeakSet
s = weakref.WeakSet()
o = C()
s.add(o)
print(s)
print(len(s))
print(o in s)
del o
gc.collect()
print(len(s))
print(o in s)
# Test weakref.finalize
a = []


def callback(arg):
    a.append(arg)


o = C()
objid = id(o)
weakref.finalize(o, callback, obj
