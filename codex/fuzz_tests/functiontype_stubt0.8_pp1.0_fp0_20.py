from types import FunctionType
a = (x for x in [1])

if isinstance(a, FunctionType):
	print 'function'
else:
	print 'not function'
