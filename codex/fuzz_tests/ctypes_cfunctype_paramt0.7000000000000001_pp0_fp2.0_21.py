import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)

class C_Callback(object):
	def __init__(self, c_function, c_args):
		self.c_function = c_function
		self.c_args = c_args

	def __call__(self, *args):
		return self.c_function(*(self.c_args + args))

def make_callback(py_function, c_args):
	c_function = FUNTYPE(py_function)
	return C_Callback(c_function, c_args)

class C_Function(object):
	def __init__(self, c_function, c_args):
		self.c_function = c_function
		self.c_args = c_args

	def __call__(self, *args):
		return self.c_function(*(self.c_args + args))

def make_function(py_function, c_args):
	c_function = FUNTYPE(py_function)
	return C_Function(c_function, c_
