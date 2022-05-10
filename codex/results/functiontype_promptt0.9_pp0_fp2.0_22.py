import types
# Test types.FunctionType for types.CodeType

def f(): pass

def deffunc(fun):
    if not isinstance(fun, types.FunctionType):
        print('Not type CHECKED')
    if not isinstance(fun.__code__, types.CodeType):
        print('Not CodeType CHECKED')

# + str(defun.)

print('deffunc(f) CHECKED ', deffunc(f))

"""
#
# Method #1
#
r34 = f.__code__
r35 = f.__code__.__doc__
r36 = f.__code__.args
r37 = f.__code__.argcount
r38 = f.__code__.posonlyargcount
r39 = f.__code__.kwonlyargcount
r40 = f.__code__.nlocals
r41 = f.__code__.stacksize
r42 = f.__code__.flags
r43 = f.__code__.co_code
r44 = f.__code__.co_consts
r45 =
