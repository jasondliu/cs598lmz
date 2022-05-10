import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# See http://docs.python.org/2/library/types.html#types.MethodType
# for details.

# The following is a hack to get around the fact that the
# __class__ attribute is not writable.  We'll just make it so
# that the __class__ attribute is a property that returns the
# class name.

def get_class_name(self):
    return self.__class__.__name__

object.__class__ = property(get_class_name)

# And now we'll make the __bases__ attribute a property that
# returns the tuple of base classes.

def get_bases(self):
    return self.__class__.__bases__

object.__bases__ = property(get_bases)

# And now we'll make the __mro__ attribute a property that
# returns the tuple of base classes.

def get_mro(self):
    return self.__class__.__mro__

