import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

fun()
 
# <__main__.CFUNCTYPE_PYOBJECT_PTR object at 0x7f4f4c4a4a40>
 
fun().value
 
# 'hello world'
 
fun()
 
# 'hello world'
 
fun() == fun()
 
# True
 
fun() == "hello world"
 
# False
 
fun() == "hello world"
 
# False
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello world"
 
# True
 
fun().value == "hello
