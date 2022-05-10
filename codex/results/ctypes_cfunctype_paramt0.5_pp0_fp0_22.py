import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(cfunc):
    return FUNTYPE(cfunc)

def make_function_from_string(cfunc_string):
    return make_function(eval(cfunc_string))

def make_function_from_file(filename):
    with open(filename, 'r') as f:
        return make_function_from_string(f.read())

def integrate_function(cfunc, start, end, nsteps):
    func = make_function(cfunc)
    step = (end - start) / nsteps
    total = 0.0
    for i in range(nsteps):
        total += func(start + i * step)
    return total * step

def integrate_function_from_string(cfunc_string, start, end, nsteps):
    return integrate_function(make_function_from_string(cfunc_string), start, end, nsteps)

def integrate_function_from_file(filename, start, end, nsteps):
    return integrate_function
