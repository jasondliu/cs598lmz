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
