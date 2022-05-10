import weakref
# Test weakref.ref

class A:
    pass

def f():
    pass

a = A()
f = f

wa = weakref.ref(a)
wf = weakref.ref(f)

weakref.getweakrefcount(a)

weakref.getweakrefs(a)

wa is None
wf()
wf() is f
