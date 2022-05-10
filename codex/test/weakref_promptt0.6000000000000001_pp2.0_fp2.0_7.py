import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r) # <weakref at 0x7f955d5b5b70; to 'C' at 0x7f955d5c9a20>
print(r()) # <__main__.C object at 0x7f955d5c9a20>

print(r() is o) # True
print(r() == o) # True

print(r() is None) # False

del o
print(r() is None) # True

print(weakref.getweakrefcount(o)) # 0
print(weakref.getweakrefs(o)) # []

try:
    print(r()) # None
except ReferenceError as e:
    print(e) # 'weakly-referenced object no longer exists'
