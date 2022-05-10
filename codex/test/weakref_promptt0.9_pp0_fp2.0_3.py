import weakref
# Test weakref.ref(package.module.function)
#

def f(a=1, b=2, c=3):
    return a + b + c

wref = weakref.ref(f)
print(wref()(10))
