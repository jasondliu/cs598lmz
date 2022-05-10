import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int )

def fun_1_to_2(): return 1, 2
def fun_2_to_1(): return (1,)

def fun_list(list): pass
def call_fun_list(): fun_list([1,2])
def paren_1_2_fun(*arglist): return arglist
def paren_list_fun(list): return list

def fun_default_value(a = 1, b = 2, c = 3): pass

def call_fun_default_value(): fun_default_value(1, 2, 3)
def call_fun_default_value(): fun_default_value(1, 2)
def call_fun_default_value(): fun_default_value(1)
def call_fun_default_value(): fun_default_value()

def fun_typed_arg(a, b : int): pass
def call_fun_typed_arg(a, b): fun_typed_arg(a, b)

def fun_vararg(*arguments): pass
def
