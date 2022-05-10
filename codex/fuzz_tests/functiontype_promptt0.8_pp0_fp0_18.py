import types
# Test types.FunctionType
import types
class Empty(object):
	pass
e = Empty()
e.__hash__ = types.FunctionType(Empty.__hash__.__code__, globals(), '__hash__', Empty.__hash__.__defaults__, Empty.__hash__.__closure__)
print e.__hash__
print type(e.__hash__)
# Test types.MethodType
import types
class Empty(object):
	pass
e = Empty()
e.__hash__ = types.MethodType(Empty.__hash__, e, Empty) # Changing the bound object
print e.__hash__
print type(e.__hash__)
print e.__hash__()
# Simultaneous TypeError and AttributeError test
import types
class Empty(object):
	pass
e = Empty()
e.__hash__ = types.MethodType(None, e, Empty) # Changing the bound object
print e.__hash__
print type(e.__hash__)
print e.__hash__()
# Test types.BuiltinFunctionType
import types
class Empty(object
