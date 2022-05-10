import weakref
# Test weakref.ref() with a custom class instance.
class C(object):
    pass

c = C()
r = weakref.ref(c)
# Test weakref.proxy() with a custom class instance.
class C(object):
    pass

c = C()
p = weakref.proxy(c)
# Test weakref.getweakrefcount() with a custom class instance.
class C(object):
    pass

c = C()
r = weakref.ref(c)
weakref.getweakrefcount(c)
# Test weakref.getweakrefs() with a custom class instance.
class C(object):
    pass

c = C()
r = weakref.ref(c)
weakref.getweakrefs(c)
# Test weakref.getweakrefs() with a custom class instance.
class C(object):
    pass

c = C()
r = weakref.ref(c)
weakref.getweakrefs(c)
# Test weakref.finalize() with a custom class instance.
class C(object):
    pass

