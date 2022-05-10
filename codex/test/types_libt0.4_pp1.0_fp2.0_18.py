import types
types.MethodType(lambda self: self.x, obj)

# Use a metaclass to add methods to a class.
class AddMethods(type):
    def __new__(cls, name, bases, dct):
        # Add a 'foo' method to the class.
        def foo(self):
            return 'foo'
        dct['foo'] = foo
        return super(AddMethods, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass__ = AddMethods

a = A()
a.foo()

# Use a metaclass to modify methods of a class.
class ModifyMethods(type):
    def __new__(cls, name, bases, dct):
        # Modify the 'bar' method of the class.
        def bar(self):
            return 'bar2'
        dct['bar'] = bar
        return super(ModifyMethods, cls).__new__(cls, name, bases, dct)

class A(object):
    __metaclass
