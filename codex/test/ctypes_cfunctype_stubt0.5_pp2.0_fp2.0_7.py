import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a):
    return "hello " + a

fun("world")

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a, b):
    return "hello " + a + " " + b

fun("world", "!")

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a, b, c):
    return "hello " + a + " " + b + " " + c

fun("world", "!", "?")

import ctypes
