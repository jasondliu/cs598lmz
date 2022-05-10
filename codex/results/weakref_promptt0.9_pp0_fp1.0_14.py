import weakref
# Test weakref.reference, including getweakrefcount

class C(object):
    pass

def callback(r):
    print repr(r)
    raise Exception("This callback function should not be called")

x = C()

n = weakref.getweakrefcount(x)
print n
# weakref.ref(x), anonymous reference with no explicit callback
weakref.ref(x)
n1 = weakref.getweakrefcount(x)
print n1
print n1 == n + 1
# weakref.ref(x, callback), referenced by a named local variable
y = weakref.ref(x, callback)
n2 = weakref.getweakrefcount(x)
print n2
print n2 == n1 + 1
# weakref.proxy(x)
z = weakref.proxy(x)
n3 = weakref.getweakrefcount(x)
print n3
print n3 == n2 + 1


class C(object):
    pass

# weakref.getweakrefs(x)
s = weakref.getweakrefs(C())
print
