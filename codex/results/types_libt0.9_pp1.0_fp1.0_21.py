import types
types.MethodType = types.MethodType
types.TypeType = types.TypeType

# Used for __specialattr__, for example for pickling
import _warnings

def builtin_id(obj):
	"""Implements the behavior of id() for builtin types"""
	
	# Ugly hack so that, e.g. type(__builtins__) == types.ModuleType and not
	# types.ModuleType. (This is because it's type(__builtins__) is set by the
	# interpreter.)
	if isinstance(obj, types.ModuleType) and obj == builtins:
		return "<module '__builtins__' (built-in)>"
	elif isinstance(obj, types.BuiltinFunctionType):
		return "<built-in function %s>" % _get_name(obj)
	elif isinstance(obj, types.BuiltinMethodType):
		return "<built-in method %s.%s of %s object>" % (
			_get_name(obj.__self__), 
			_get_
