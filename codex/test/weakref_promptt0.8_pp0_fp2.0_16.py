import weakref
# Test weakref.ref(foo) vs. weakref.proxy(foo)
# This will print:
#   weakref.ref(foo) returns <weakref at 000000030D4A8EC8; dead>
#   weakref.proxy(foo) raises ReferenceError

class Foo(object):
    def __init__(self, name):
        self.name = name

class Bar(object):
    def __init__(self, foo):
        self._foo = weakref.proxy(foo)

foo = Foo("Foo")
bar = Bar(foo)

del foo
try:
    bar._foo.name # AttributeError: 'Foo' object has no attribute 'name'
except ReferenceError:
    print("weakref.proxy(foo) raises ReferenceError")
else:
    print("weakref.proxy(foo) returns", repr(bar._foo))

bar2 = Bar(foo)
del foo
