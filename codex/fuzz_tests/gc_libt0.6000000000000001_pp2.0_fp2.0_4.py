import gc, weakref

#from gc import get_threshold, set_threshold

class C(object):
    pass

def get_rp():
    return gc.get_referrers(C)

r = get_rp()

print(type(r))
print(len(r))
print(len(r[0]))

set_threshold(1, 1, 1)

class C(object):
    def __del__(self):
        pass

a = C()
b = C()

a.x = b
b.x = a

set_threshold(0, 0, 0)

del a, b

#print(get_rp())

print(gc.collect())
print(len(gc.garbage))
print(gc.garbage[0])

def f():
    a = C()
    a.x = C()
    a.x.x = a

f()

print(gc.collect())
print(len(gc.garbage))
print(gc.garbage[0])
