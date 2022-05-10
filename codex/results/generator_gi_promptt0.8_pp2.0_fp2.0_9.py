gi = (i for i in ())
# Test gi.gi_code.co_filename

# Test with code_obj
def func():
	pass
co = func.func_code

assert co.co_filename

# Test with PyCodeObject
import ctypes

def make_new_code():
	# Make a new code object
	def MakeCode(argcount, nlocals, stacksize, flags, codestring, constants,
			     names, varnames, filename, name, firstlineno, lnotab,
			     freevars, cellvars) :
		return type(co)(argcount, nlocals, stacksize, flags, codestring,
						constants, names, varnames, filename, name,
						firstlineno, lnotab, freevars, cellvars)

	PyCode_New = ctypes.pythonapi.PyCode_New
	PyCode_New.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.py_object, 

