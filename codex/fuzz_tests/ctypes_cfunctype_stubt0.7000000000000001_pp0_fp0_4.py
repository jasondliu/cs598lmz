import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():return
def f():
    for i in range(200000):
        fun()
t = time.time()
f()
print(time.time()-t)

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():return
def f():
    for i in range(200000):
        fun()
t = time.time()
f()
print(time.time()-t)


import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():return
def f():
    for i in range(200000):
        fun()
t = time.time()
f()
print(time.time()-t)
