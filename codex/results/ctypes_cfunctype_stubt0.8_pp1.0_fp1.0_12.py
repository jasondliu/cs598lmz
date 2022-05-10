import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello")
    return 1

print(fun.argtypes,fun.restype)
print(fun.__code__.co_argcount)

###########
print("\n\n")
@send_args_to_first
def bar(a,b):
    print(a,b)

@bar
def foo(a,b):
    print(a,b)

foo(3,4)

############
print("\n\n")

@send_kwargs_to_first
def bar(**kwargs):
    print(kwargs["a"],kwargs["b"])

@bar
def foo(**kwargs):
    print(kwargs["a"],kwargs["b"])

foo(a=3,b=4)

##############
print("\n\n")
def func(a,b):
    return a+b

print(inspect.getfullargspec(func))
print(inspect.getargspec(func))
print(inspect.getcallargs(func,3,4
