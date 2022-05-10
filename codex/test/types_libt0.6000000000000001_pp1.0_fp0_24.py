import types
types.new_class("MyClass")

# Now let's create a couple instances of this new class
obj1 = MyClass()
obj2 = MyClass()

# And let's add a couple fields to each instance
obj1.foo = 1
obj2.foo = 2

# And let's add a couple methods
def foo1(self):
    return self.foo
def foo2(self):
    return self.foo*2

obj1.bar = types.MethodType(foo1, obj1)
obj2.bar = types.MethodType(foo2, obj2)

print(obj1.bar()) # 1
print(obj2.bar()) # 4
