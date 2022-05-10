import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
ctypes.CDLL('./libexample.so').sin.restype = FUNTYPE
ctypes.CDLL('./libexample.so').cos.restype = FUNTYPE

import sharedlib_example

sin = ctypes.CDLL('./libexample.so').sin
sin = sin()
cos = ctypes.CDLL('./libexample.so').cos
cos = cos()

print(sin, cos)
print(sharedlib_example.sin, sharedlib_example.cos)
</code>
The output is empty. What I want is a thing like <code>&lt;_FuncPtr object at 0x7f95dafa14f0&gt;</code> respectively
<code>&lt;_FuncPtr object at 0x7f95dafa1558&gt;</code>. 
How can I retrieve the name of the function pointer?


A:

Read about inlining and optimization. Usually, after optimization, all exported functions become local. 
If you really want to be sure, recomp
