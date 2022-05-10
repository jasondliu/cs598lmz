import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

# Read in and execute the C++ implementation of the things we need
with open(os.path.join(THIS_DIRECTORY, 'injective_set.cpp')) as f:
	c_code = f.read()
	c_code_obj = compile(c_code, '<string>', 'exec')
	exec(c_code_obj)

# Create some useful objects
c_lib = CDLL(os.path.join(THIS_DIRECTORY, 'injective_set'))

# Expose these objects to the user
__all__ = ['InjectiveSet','c_lib','FUNTYPE']
