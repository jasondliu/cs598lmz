import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_void_p)

function_address = lib.get_function_address('f')
lib.register_function(function_address, FUNTYPE(function))

# Create a gradient function
def grad_function(rhs, wrt):
    wrt = wrt.ravel()
    rhs = rhs.ravel()

    derivs = [0.0 for i in range(len(wrt))]
    for i, x in enumerate(wrt):
        dx = pow(x, 3)*1e-7
        if x == 0.0:
            dx = 1e-7
        derivs[i] = (function(wrt+dx)-function(wrt-dx))/dx/2

    return np.array(derivs).reshape(rhs.shape)

# Test the gradient
print(grad_function(0.0, np.array([1.0])))

# Register the gradient function
function_address = lib.get_function_address('fg')
lib.register_function(function_address
