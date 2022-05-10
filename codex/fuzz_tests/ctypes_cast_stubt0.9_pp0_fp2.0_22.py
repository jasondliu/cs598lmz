import ctypes
ctypes.cast(0, ctypes.py_object)
 
# prints "c_void_p(None)"
 
# ...and you get the sigsegv anyway
【解决过程】
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

# ctypes.c_void_p(0) gives access violation
import ctypes
ctypes.cast(0, ctypes.c_void_p)
 
# This also works
import ctypes
ctypes.cast(0, ctypes.py_object)
 
# prints "c_void_p(None)"
 
# ...but you don't get the sigsegv any more
 
# the following works...
ctypes.c_void_p(1)
 
# but this doesn't
ctypes.c_void_p(-1)
 
# so changing the value of Py_None
