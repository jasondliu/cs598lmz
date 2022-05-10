import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")

# 将python对象转换成C对象
c_fun = FUNTYPE(fun)

# 将C对象转换成python对象
py_fun = ctypes.pythonapi.PyCFunction_NewEx(c_fun, None, None)
print(py_fun)
print(py_fun.__call__())

# 将python对象转换成C对象
c_fun = FUNTYPE(py_fun)
print(c_fun)
print(c_fun())
