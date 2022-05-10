import weakref
# Test weakref.ref documentation
class MyClass(object):
    pass

ob = MyClass()
ref = weakref.ref(ob)
ob2 = ref()
print(ob2 is ob)
print(ob2 == ob)
print(ob2)
print(ob)
print(ref)

print(ref.__class__)

print(ref.__eq__)

print(ref.__hash__)

print(ref.__init__)

print(ref.__repr__)

print(ref.__call__)

print(ref.__str__)
