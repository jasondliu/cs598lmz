import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, None)
with open('c_code.txt') as f:
    libs_and_funcs = compile_libraries(f)
libraries, functions = libs_and_funcs
print(functions)

def python_func(x, y=None):
    return 2*x

c_code = """
{}
void python_func(double *x, double *py_val) {{ *py_val = py_func(x[0]); }}
"""

with open('python_code.txt') as f:
    libs_and_funcs = compile_libraries(f, functions={'py_func': python_func})
libraries, functions = libs_and_funcs
print(functions)

libs_and_funcs = compile_libraries(StringIO(c_code.format(c_code)), global_vars=dict(py_func=python_func))
libraries, functions = libs_and_funcs
print(functions)

def func(
