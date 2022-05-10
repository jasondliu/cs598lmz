import weakref
# Test weakref.ref
# from weakref import ref
class klass:
    pass
inst = klass()
r = weakref.ref(inst)
print r.key
# Test weakref.proxy
# from weakref import proxy
class klass:
    pass
inst = klass()
r = weakref.proxy(inst)
# Test weakref.getweakrefcount
# from weakref import getweakrefcount
class klass:
    pass
inst = klass()
r = weakref.ref(inst)
print weakref.getweakrefcount(inst)
# Test weakref.getweakrefs
# from weakref import getweakrefs
class klass:
    pass
inst = klass()
r = weakref.ref(inst)
print weakref.getweakrefs(inst)
# Test weakref.WeakSet
# from weakref import WeakSet
class klass:
    pass
inst = klass()
s = weakref.WeakSet()
s.add(inst)
print len(s)
# Test weakref.WeakKeyDictionary
# from weakref import Weak
