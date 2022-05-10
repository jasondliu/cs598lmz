import types
types.FunctionType
types.MethodType
types.ClassType
None

# hashable
isinstance("", types.StringTypes)
type("")
issubclass(type(""), types.StringTypes)

# tuple, list, dict, and set.
# instances of those types are not hashable by default.

