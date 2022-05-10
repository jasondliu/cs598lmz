import weakref
# Test weakref.ref()

class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(' + self.name + ')'

o = C('o')
r = weakref.ref(o)
print('o:', o)
print('ref:', r)
print('r():', r())
print('deleting o')
del o
print('r():', r())
print('r():', r())

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o = C('o')
d['o'] = o
print('d["o"]:', d['o'])
print('deleting o')
del o
print('d["o"]:', d['o'])
print('d["o"]:', d['o'])
