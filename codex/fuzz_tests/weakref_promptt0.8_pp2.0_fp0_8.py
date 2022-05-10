import weakref
# Test weakref.ref() and weakref.proxy()
class C:
    pass
def print_by_ref(r):
    print("r:",r(),r)
def print_by_proxy(p):
    try:
        print("p:",p,p())
    except ReferenceError:
        print("p: dead")
o=C()
print("o:",o)
r=weakref.ref(o)
print_by_ref(r)
print_by_proxy(r)
p=weakref.proxy(o)
print_by_ref(r)
print_by_proxy(r)
print_by_proxy(p)
o2=o
r2=weakref.ref(o2)
print_by_ref(r)
print_by_ref(r2)
del o2
print_by_ref(r)
print_by_ref(r2)

print("######iterate over a weakref#####")
class C:
    pass
def print_by_ref(r):
    print("r:",r(),r)

