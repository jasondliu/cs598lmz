import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise SystemError
# The following checks that object.__new__(catcher) does not call repr
# on catcher, by passing it a class whose repr raises an exception.
if re.match("<type 'type'>", repr(type(fun))):
    raise SystemError

# Testing PySequence_Fast_* functions
eq = []

def FAST_add_item(o, i):
    eq.append(1)

def FAST_del_item(o, i):
    eq.append(2)

def FAST_concat(o1, o2):
    eq.append(3)

def FAST_repeat(o1, i):
    eq.append(4)

def FAST_inplace_concat(o1, o2):
    eq.append(5)

def FAST_inplace_repeat(o1, i):
    eq.append(6)

def LIST_setitem(o, i, v):
    eq.append(7)

def LIST_delitem(o, i):
    eq.
