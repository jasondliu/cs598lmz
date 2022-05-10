import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a+b

def func2(a, b):
    return a-b

def func3(a, b):
    return a*b

def func4(a, b):
    return a/b

def func5(a, b):
    return a%b

def func6(a, b):
    return a**b

def func7(a, b):
    return a&b

def func8(a, b):
    return a|b

def func9(a, b):
    return a^b

def func10(a, b):
    return a<<b

def func11(a, b):
    return a>>b

def func12(a, b):
    return a<b

def func13(a, b):
    return a<=b

def func14(a, b):
    return a>b

def func15(a, b):
    return a>=b

def func16(a, b):
    return a
