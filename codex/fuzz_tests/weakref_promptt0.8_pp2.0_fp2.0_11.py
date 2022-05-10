import weakref
# Test weakref.ref and weakref.proxy objects

class SomeObj:
    pass

def callback(obj):
    print('obj deleted!')

x = SomeObj()
x.attr = 10

objref = weakref.ref(x, callback)
print(objref())
print(objref() is None)

objref = weakref.proxy(x, callback)
print('attr -- ', objref.attr)
print(objref)

# WeakValueDictionary

obj = SomeObj()
obj.attr = 10

d = weakref.WeakValueDictionary()
d[1] = obj
print(d[1].attr)

obj = SomeObj()
obj.attr = 20
d[2] = obj
print(d[2].attr)

print(d[1].attr)
