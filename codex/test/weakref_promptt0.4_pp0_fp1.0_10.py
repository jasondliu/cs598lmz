import weakref
# Test weakref.ref() with a class that defines a __del__ method.
class C:
    def __del__(self):
        print("deleting C")

def f():
    print("f()")

c = C()
r = weakref.ref(c, f)
print("created ref")
del c
print("deleted c")
print("del ref")
del r
print("done")

# created ref
# deleted c
# del ref
# f()
# deleting C
# done
