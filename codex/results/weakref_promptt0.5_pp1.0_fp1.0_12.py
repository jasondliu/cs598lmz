import weakref
# Test weakref.ref
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<C %s>" % self.x

c = C(1)
r = weakref.ref(c)
print r
print r()
print r() is c

c = C(2)
print r()
print r() is None

print "-"*40

# Test weakref.WeakValueDictionary
class C:
    cnt = 0
    def __init__(self):
        C.cnt += 1
    def __del__(self):
        C.cnt -= 1

c1 = C()
c2 = C()
d = weakref.WeakValueDictionary()
d['c1'] = c1
d['c2'] = c2
print d
print d['c1']
print d['c2']
print d.items()
print C.cnt
del c1
print C.cnt
print d
print d['c2']
print d.items()
del c
