import types
types.MethodType(foo, None, None)

# Test that we can bind a method to an object that does not have the attribute
# yet.
class A:
    pass

a = A()
a.foo = foo

def bar():
    print("bar")

a.bar = types.MethodType(bar, a)
a.bar()

# Test that we can bind a method to an object that already has the attribute.
class A:
    def bar(self):
        print("bar")

a = A()
a.foo = foo
a.foo()

a.bar = types.MethodType(bar, a)
a.bar()

# Test that we can bind a method to an object that already has the attribute
# with the same name.
class A:
    def bar(self):
        print("bar")

a = A()
a.foo = foo
a.foo()

a.bar = types.MethodType(bar, a)
a.bar()

# Test that we can bind a method to an object that already has the attribute
# with
