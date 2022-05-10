import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def fun():
    return 1

print(type(fun))
print(fun())
print("\n")


def fun():
    return 1

print(type(fun))
print(fun())
print("\n")



def fun():
    def fun2():
        return 2
    return fun2

print(type(fun))
print(type(fun()))
print(fun)
print(fun())
print(fun()())
print("\n")



def fun():
    def fun2():
        return 2
    return fun2

print(type(fun))
print(type(fun()))
print(fun)
print(fun())
print(fun()())
print("\n")



def fun():
    def fun2():
        def fun3():
            return 3
        return fun3
    return fun2

print(type(fun))
print(type(fun()))
print(type(fun()()))
print(fun)
print(fun())
print(fun()())
print(fun()
