from types import FunctionType
a = (x for x in [1])
type(a)

b = FunctionType(a.gi_code, {})
type(b)

b = lambda: a
a = b.__closure__[0]

# hmm, this is not very pretty...

# ctypes.pythonapi.PyFrame_New()

# pythonapi.PyCode_New(arg1, arg2, arg3, arg4, arg5, arg6, arg7)


# pythonapi.PyEval_EvalCodeEx(_ctypes.PyObject)


# 参见:
# https://stackoverflow.com/questions/1769403/find-out-if-object-is-a-generator
# https://stackoverflow.com/questions/966070/how-to-convert-a-python-generator-to-a-function
