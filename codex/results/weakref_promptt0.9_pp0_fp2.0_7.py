import weakref
# Test weakref.ref
# See also test_weakref.py

def callback(w, r):
    print("callback(", w, r, ")")
def check(r):
    print("check(", r, ")")
    if r:
        print(r())
    else:
        print("<None>")

print("Create some weak references")
a = A()
a.b = B()
a.b.a = a

print("Create the weakrefs")
a_ref = weakref.ref(a)
a_b_ref = weakref.ref(a.b)
a_b_weakref = a.b.a_ref = weakref.ref(a)

print("Get the referents")
check(a_ref)
check(a_b_ref)

print("Delete a and b")
del a
del a.b

print("Collect garbage")

import gc
gc.collect()

print("Check the referents again")
check(a_ref)
check(a_b_ref)

print("
