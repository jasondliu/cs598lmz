import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double),
                           ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))

def callback_func(x, n_x, f, user_data):
    print("%d-D callback with user_data %d" % (n_x, int(user_data)))
    return x[0]*x[0]

if __name__ == '__main__':
    nlopt.srand(100)

    f = FUNTYPE(callback_func)
    user_data = ctypes.c_void_p(42)

    opt = nlopt.opt(nlopt.LN_COBYLA, 1)
    opt.set_min_objective(f, user_data)
    opt.set_lower_bounds([-1])
    opt.set_upper_bounds([1])
    opt.set_xtol_rel(1e-4)
    x = opt.optimize([0.234])
    ret = opt
