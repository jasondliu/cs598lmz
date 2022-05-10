import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst

# weakref.ref(object[,callback])
# weakref.proxy(object,callback)
# - create a weak reference and return a weak reference object.
# - callback: called when the referenced object is deleted.
# - weakref.proxy(object) returns a proxy object.

# weakref.getweakrefcount(object)
# - return the number of weak references to the object.

# weakref.getweakrefs(object)
# - return a list of weak reference objects for the given object.

# weakref.proxy(object[,callback])
# - same as weakref.proxy(object,callback)

from weakref import WeakKeyDictionary
class Cheese(object):pass
# dict subclass that only allows hashable keys
stock=WeakKeyDictionary()
catalog=[Cheese() for i in range(10)]
for cheese in catalog:
    stock[cheese]=cheese

# WeakValueDictionary
# - subclass of dict that only allows hashable keys
