import ctypes
# Test ctypes.CFUNCTYPE

# prototypes of the functions we want to call
prototype = ctypes.CFUNCTYPE (ctypes.c_int, ctypes.c_int)

# list of the parameters we want to pass
params = (ctypes.c_int,)

print '\n*** Testing ctypes.CFUNCTYPE'

class Test_CFuntype:
    def __init__(self, func):
        self.func = func

    def __call__(self, arg):
        return self.func(arg)

# callback as an object
test_obj = Test_CFuntype (lambda x: x*x)
test_obj_addr = ctypes.cast (id (test_obj), ctypes.c_void_p).value
print '    obj_addr:{0}  obj(2):{1}'.format (test_obj_addr, test_obj(2))

# callback as a bound method
test_bound = Test_CFuntype (lambda x: x*x).__call__
test_bound_addr = ctypes.cast (id (test_bound
