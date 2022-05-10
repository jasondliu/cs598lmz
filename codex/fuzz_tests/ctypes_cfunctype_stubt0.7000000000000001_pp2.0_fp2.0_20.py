import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "fun()"
    return 0

def fun2():
    print "fun2()"

# fun2.__lt__ = fun
fun2.__lt__ = fun
fun2.__gt__ = fun
fun2.__le__ = fun
fun2.__ge__ = fun
fun2.__eq__ = fun
fun2.__ne__ = fun
fun2.__add__ = fun
fun2.__sub__ = fun
fun2.__mul__ = fun
fun2.__floordiv__ = fun
fun2.__mod__ = fun
fun2.__divmod__ = fun
fun2.__pow__ = fun
fun2.__lshift__ = fun
fun2.__rshift__ = fun
fun2.__and__ = fun
fun2.__xor__ = fun
fun2.__or__ = fun

fun2()
print fun2 < fun2
print fun2 > fun2
print fun2 <= fun2
print fun2 >= fun2
print fun2 == fun2
print fun2 != fun2
print fun
