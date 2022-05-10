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

# In [41]: hash((1,2,(2,3)))
# Out[41]: 10976365022236648375365256092394014491392
# In [43]: d = {}
# In [44]: d[(1,2,(2,3))] = 5
# In [45]: d
# Out[45]: {(1, 2, (2, 3)): 5}
