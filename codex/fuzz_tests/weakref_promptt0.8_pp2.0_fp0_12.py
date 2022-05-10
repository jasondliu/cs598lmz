import weakref
# Test weakref.ref()
b = Base()
ref = weakref.ref(b)
b.foo(1)
b.bar(2)
raise Exception()
