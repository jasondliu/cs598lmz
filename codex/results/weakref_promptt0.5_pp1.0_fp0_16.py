import weakref
# Test weakref.ref(object)
class C: pass
c = C()
r = weakref.ref(c)
print r
# Test weakref.ref(object, callback)
class C: pass
c = C()
l = []
def callback(arg): l.append(arg)
r = weakref.ref(c, callback)
print r
# Test weakref.proxy(object)
class C: pass
c = C()
p = weakref.proxy(c)
print p
# Test weakref.proxy(object, callback)
class C: pass
c = C()
l = []
def callback(arg): l.append(arg)
p = weakref.proxy(c, callback)
print p
# Test weakref.getweakrefcount
class C: pass
c = C()
print weakref.getweakrefcount(c)
# Test weakref.getweakrefs
class C: pass
c = C()
print weakref.getweakrefs(c)
# Test WeakKeyDictionary
d = weakref.WeakKeyDictionary()
class C: pass
c =
