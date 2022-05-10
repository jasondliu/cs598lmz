import types
types.MethodType(lambda self: None, None, Foo)

# A method can be called on an instance of its class
Foo().bar()

# A method can be called on any instance of a subclass of its class
class SubFoo(Foo):
    pass
SubFoo().bar()

# A method can be called on an instance of any class with the method
class Other(object):
    def bar(self):
        pass
Other().bar()

# A method can be called on an instance of any class as long as the method
# doesn't use `self`
class OtherWithSelf(object):
    def bar(self):
        print(self)
OtherWithSelf().bar()

# A method can be called on an instance of any class as long as the method
# doesn't use `self`
