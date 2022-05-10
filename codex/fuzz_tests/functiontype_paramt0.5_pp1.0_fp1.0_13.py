from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo').__closure__)
# [<cell at 0x7f8f48c3a708: int object at 0x7f8f48cef9a0>]

# now, let's try to do the same with a function
# declared in a class
class Foo(object):
    def bar(self):
        return self

list(Foo.bar.__closure__)
# [<cell at 0x7f8f48c3a6e8: Foo object at 0x7f8f48c3a690>]
# and it works the same way!

# but what about the function defined in the class
# that uses a closure?
class Foo(object):
    def bar(self):
        self.foo = lambda: self

Foo().bar().foo().bar()
# <__main__.Foo object at 0x7f8f48c3a8d0>

# and now, let's try to use __closure__
list(Foo.bar.__closure__)
# AttributeError: 'function
