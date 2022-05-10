from types import FunctionType
list(FunctionType(add.__code__, {'print':print}, "add", ("x", "y", ), ("print", )))
# <function add at 0x1068f8510>

class FunctionType(object):
	def __init__(self, code, globals, name, argdefs, closure):
		# "argdefs" has to be a tuple if is not None
		self.__code__ = code
		self.__name__ = name or code.co_name
		self.__dict__ = {}
		self.__defaults__ = None
		self.__globals__ = globals
		self.__closure__ = closure
		self.__doc__ = code.co_consts[0] if code.co_consts else None

		# if there is any __kwdefaults__ in argdefs, then self.__keywords__
		if argdefs:
			# print a tuple of names
			self.__kwdefaults__ = argdefs.__kwdefaults__
			# print
