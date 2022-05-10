import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.c_int)


def make_func(func):
    args = ()
    if func.__name__ == 'mysum':
        def f(data, i_data, count):
            args = tuple(data[:count])
            return func(*args)
    elif func.__name__ == 'quicksort':
        def f(data, i_data, count):
            args = (data, i_data, count)
            func(*args)
            return 0
    else:
        def f(data, i_data, count):
            args = (data, count)
            return func(*args)
    return FUNTYPE(f)


def test_function(func, f_name, func_args):
    # Build argument values.
    arg_values = [np.random.randint(-10, 10, size=size)
                  for size in func_args]

