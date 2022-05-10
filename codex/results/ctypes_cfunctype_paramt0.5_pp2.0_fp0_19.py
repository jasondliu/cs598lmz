import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_func(name):
    return FUNTYPE(lib.get_func(name))

def get_func_list(name):
    return [get_func(n) for n in name]

funcs = get_func_list(['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'])

def f(x):
    return [func(x) for func in funcs]

def df(x):
    return [func(x) for func in dfuncs]

dfuncs = get_func_list(['df1', 'df2', 'df3', 'df4', 'df5', 'df6', 'df7', 'df8'])

def f(x):
    return [func(x) for func in funcs]

def df(x):
    return [func(x) for func in dfuncs]

def g(x):
    return -f(x)


