import weakref
# Test weakref.ref()

# Create a weakref to an object
class Foo:
    pass

foo = Foo()
ref = weakref.ref(foo)

# Create a weakref to a function
def bar():
    pass

ref = weakref.ref(bar)

# Create a weakref to a method
class Foo:
    def bar(self):
        pass

foo = Foo()
ref = weakref.ref(foo.bar)

# Create a weakref to a builtin function
ref = weakref.ref(len)

# Create a weakref to a builtin method
ref = weakref.ref([].append)

# Create a weakref to a class
ref = weakref.ref(Foo)

# Create a weakref to a class method
class Foo:
    @classmethod
    def bar(cls):
        pass

ref = weakref.ref(Foo.bar)

# Create a weakref to a static method
class Foo:
    @staticmethod
    def bar():
        pass

