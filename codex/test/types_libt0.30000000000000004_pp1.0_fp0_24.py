import types
types.MethodType(lambda self: None, None, None)

# This is a test of the new-style class syntax.
# The class is called 'Foo' and inherits from 'object'.
class Foo(object):
    # This is a class attribute.
    bar = 1

    # This is a method.
    def baz(self, x):
        # This is a local variable.
        y = x + 1
        return y

# This is a test of the old-style class syntax.
# The class is called 'Foo' and inherits from 'object'.
class Foo:
    # This is a class attribute.
    bar = 1

    # This is a method.
    def baz(self, x):
        # This is a local variable.
        y = x + 1
        return y

# This is a test of the old-style class syntax.
# The class is called 'Foo' and inherits from 'object'.
class Foo:
    # This is a class attribute.
    bar = 1

