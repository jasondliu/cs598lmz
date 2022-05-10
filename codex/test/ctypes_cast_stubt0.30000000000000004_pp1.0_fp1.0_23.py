import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a test of the new-style class syntax.
class NewStyleClass(object):
    pass

# This is a test of the old-style class syntax.
class OldStyleClass:
    pass

# This is a test of the new-style class syntax with a metaclass.
class NewStyleClassWithMeta(object):
    __metaclass__ = type

# This is a test of the old-style class syntax with a metaclass.
class OldStyleClassWithMeta:
    __metaclass__ = type

# This is a test of the new-style class syntax with a metaclass that's
# not type.
class NewStyleClassWithNonTypeMeta(object):
    __metaclass__ = object

# This is a test of the old-style class syntax with a metaclass that's
# not type.
class OldStyleClassWithNonTypeMeta:
    __metaclass__ = object

# This is a test of the new-style class syntax with a metaclass that's
# not type, but is
