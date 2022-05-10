import weakref
# Test weakref.ref(o)

try:
    ref
except NameError:
    import sys
    print("SKIP")
    sys.exit()

class A(object):
    pass

class B(object):
    def __init__(self, x):
        self.x = x

# Test weakref.ref(o)
a = A()
a_ref = ref(a)
print(a_ref())
print(a_ref() is a)

print(weakref.getweakrefcount(a))
print(weakref.getweakrefs(a))

b = B(a)
b_ref = ref(b)
print(b_ref().x)
print(b_ref().x is a)

print(weakref.getweakrefcount(a))
print(weakref.getweakrefs(a))

# Test weakref.ref(o, callback)
def callback(obj):
    print("callback")

c = A()
c_ref = ref(c, callback)
print(c_ref())
print(c_ref
