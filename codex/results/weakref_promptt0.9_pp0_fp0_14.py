import weakref
# Test weakref.ref():
def f():
    return "we don't want this to show up"
class C:
    pass

c = C()
print(c.__class__)
r = weakref.ref(c)
print(r)
del c
print(r)
print(r())

print('-'*10, 'weakref.proxy()', '-'*10)

sl = weakref.WeakValueDictionary()
def expunge(ref):
    try:
        del sl[ref.key]
#         print('unreferenced object', ref.key)
    except KeyError:
        pass

class C:
    def __init__(self, key):
        self.key = key
        sl[key] = self
    def __del__(self):
        expunge(self)
        
a = C('a')
b = C('b')
d = weakref.WeakKeyDictionary()

d['a'] = a
d['b'] = b

print(sorted(sl))
print(sorted(d))

del
