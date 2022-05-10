import weakref
# Test weakref.ref(A())
class A:
    def __del__(self):
        print("deleted")

ref= weakref.ref(A())
del ref

# Test weakref.finalize(A(), A.__del__)
finalize= weakref.finalize(A(), A.__del__)
del finalize

# Test weakref.proxy(A())
class B:
    def __init__(self):
        self.x= 1

p= weakref.proxy(B())
p.x= 2
print(p.x)

# Test weakref.getweakrefcount(A())
print(weakref.getweakrefcount(A()))

# Test weakref.getweakrefs(A())
print(weakref.getweakrefs(A()))

# Test weakref.ref(B())
class C:
    def __del__(self):
        print("deleted")

ref= weakref.ref(C())
del ref

# Test weakref.finalize(B(), B.__del__)
