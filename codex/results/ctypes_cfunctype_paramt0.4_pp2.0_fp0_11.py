import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def compile_function(expr, varname='x'):
    return FUNTYPE(expr.compile(varname))

def compile_function_with_derivative(expr, varname='x'):
    return FUNTYPE(expr.compile(varname)), FUNTYPE(expr.diff(varname).compile(varname))

def compile_function_with_derivative_and_second_derivative(expr, varname='x'):
    return FUNTYPE(expr.compile(varname)), FUNTYPE(expr.diff(varname).compile(varname)), FUNTYPE(expr.diff(varname).diff(varname).compile(varname))

def compile_function_with_derivative_and_second_derivative_and_third_derivative(expr, varname='x'):
    return FUNTYPE(expr.compile(varname)), FUNTYPE(expr.diff(varname).compile(varname)), FUN
