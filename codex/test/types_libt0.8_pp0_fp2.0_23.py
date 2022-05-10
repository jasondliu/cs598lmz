import types
types.ClassType


# This shows a singleton is mutable.
null_object = object()
null_object.__class__ = int
