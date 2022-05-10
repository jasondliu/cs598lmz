import types
types.ClassType = ClassType
types.TypeType = TypeType
types.InstanceType = InstanceType

print ' --- class types'
print type(C)       == ClassType
print type(c)       == InstanceType
print type(D)       == ClassType
print type(d)       == InstanceType
print type(c.__str__) == types.MethodType
print type(long)    == ClassType
print type(10L)     == types.LongType
print type(range(10)) == types.ListType
print type({})      == types.DictType
print type(())      == types.TupleType
print type([])      == types.ListType

print ' --- subclass types'
print issubclass(type(c), C)
print issubclass(type(c), InstanceType)
print issubclass(type(d), D)
print issubclass(type(d), InstanceType)

print ' --- type tests'
print isinstance(c, C)
print isinstance(d, D)
print isinstance(c, InstanceType)
