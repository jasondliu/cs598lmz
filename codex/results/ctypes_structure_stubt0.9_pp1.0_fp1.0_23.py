import ctypes

class S(ctypes.Structure):
    x = 0
    y = 0
    z = 0
    w = 0
</code>


A:

In short, ctypes doesn't do so called implicit conversions like C does. C-types are mapped one to one. For example a C-function like
<code>void func(int* p) {
    *p = 5;
}
</code>
can be mapped to Python as
<code>from ctypes import *

lib = CDLL('./lib.so')
lib.func.argtypes = [POINTER(c_int)]
p = c_int(0)
lib.func(byref(p)) 
</code>
but the <code>p</code> variable used here is a <code>c_int</code> not a <code>c_int*</code> and can't be dereferenced.
You can map the structure to the Pyhton-Type using a <code>Structure</code> subtype:
<code>from ctypes import *

class Point(Structure):
    _fields_ = [('x',c_int), ('
