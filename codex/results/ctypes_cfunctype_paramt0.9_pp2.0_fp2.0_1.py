import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)
name = 'hello'
value = 'here'

@FUNTYPE
def _fun(msg):
    print(msg)

# 把c语言函数注册到python
lib.register(name, _fun)
# 调用c语言上注册的函数
lib.callFunc(name)
"""

"""
with open("./libhello.so", "wb") as out_file:
    out_file.write(source_list)

import os
os.system("python setup.py build_ext --inplace")
"""
