import types
types.CodeType

def f(x):
    return x**2

#f.__code__
#f.__code__.co_code
#f.__code__.co_consts

#f.__code__.co_code.__class__
#f.__code__.co_consts.__class__

#f.__code__.co_code[1].__class__
#f.__code__.co_consts[0].__class__

def g(x):
    return x**4

#f.__code__.co_code == g.__code__.co_code

#f.__code__.co_consts == g.__code__.co_consts

#f.__code__.co_code
#b'|\x00|\x01\x17\x00S\x00'
#f.__code__.co_consts
#(None, 2)
