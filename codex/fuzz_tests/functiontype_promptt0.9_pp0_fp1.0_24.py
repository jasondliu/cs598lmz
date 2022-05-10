import types
# Test types.FunctionType(fn, globals=)
# Test types.FunctionType.__doc__
if 1:
	x = 123
	def func():
		return x
	f = types.FunctionType(func.func_code, globals(), "temp", func.func_defaults, func.func_closure)
	if f.__doc__ != "temp": print f.__doc__
	if f() != 123: print f()
	
	func.func_code = f.func_code
	func.func_defaults = f.func_defaults
	func.func_closure= f.func_closure
	if func() != 123: print func()
