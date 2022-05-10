import types
types.MethodType(lambda self: self.x, None)

# The following is a regression test for SF bug #817397.
# It checks that the __new__ method of a metaclass is called
# when the metaclass is used to create a class.

class Meta(type):
    def __new__(meta, name, bases, dict):
        return type.__new__(meta, name, bases, dict)

class Foo(object):
    __metaclass__ = Meta

# The following is a regression test for SF bug #817448.
# It checks that the __new__ method of a metaclass is called
# when the metaclass is used to create a class.

class Meta(type):
    def __new__(meta, name, bases, dict):
        return type.__new__(meta, name, bases, dict)

class Foo(object):
    __metaclass__ = Meta

# The following is a regression test for SF bug #817448.
# It checks that the __new__ method of a metaclass is called
# when
