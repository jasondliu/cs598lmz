import types
# Test types.FunctionType, types.ClassType, and types.MethodType
class FunctionType:
	def __init__(self):
		pass
class ClassType:
	def __init__(self):
		pass
	def method(self):
		pass
def function():
	return 0
# Test isinstance
assert isinstance(FunctionType, types.ClassType)
assert isinstance(ClassType, types.ClassType)
assert isinstance(0, types.IntType)
assert isinstance(0.0, types.FloatType)
assert isinstance("", types.StringType)
assert isinstance(slice(0), types.SliceType)
assert isinstance([], types.ListType)
assert isinstance({}, types.DictType)
assert isinstance(0+0j, types.ComplexType)
assert isinstance(tuple(), types.TupleType)
assert isinstance(True, types.BooleanType)
assert isinstance(long(0), types.LongType)
assert isinstance(ClassType().method, types.MethodType)
assert isinstance([].append, types.Function
