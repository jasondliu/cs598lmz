import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

class C:
    pass

@FUNTYPE
def fun(c):
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
    c.x = 2
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
    c.x = 2
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
    c.x = 2
    return c.x

c = C()
c.x = 1
fun(c)

@FUNTYPE
def fun(c):
   
