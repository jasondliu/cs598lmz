import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def test1(a, b):
    return a + b

def test2(a, b):
    return a - b

def test3(a, b):
    return a * b

def test4(a, b):
    return a / b

def test5(a, b):
    return a ** b

def test_print(a, b):
    print a, b

fun1 = FUNTYPE(test1)
fun2 = FUNTYPE(test2)
fun3 = FUNTYPE(test3)
fun4 = FUNTYPE(test4)
fun5 = FUNTYPE(test5)
fun6 = FUNTYPE(test_print)

print fun1(2,3)
print fun2(2,3)
print fun3(2,3)
print fun4(2,3)
print fun5(2,3)
fun6(2,3)
</code>
So, you can use all test function in your ctypes function type without writing
