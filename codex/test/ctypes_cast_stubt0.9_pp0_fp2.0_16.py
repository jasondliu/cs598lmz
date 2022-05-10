import ctypes
ctypes.cast(ctypes.c_void_p.from_param(23), ctypes.py_object)
# &lt;__main__.LP_py_object object at 0x7f87145c7930&gt;
ctypes.cast(23, ctypes.py_object)
# &lt;__main__.LP_py_object object at 0x7f87145c7930&gt;
ctypes.cast(23, ctypes.py_object).value
# 23
