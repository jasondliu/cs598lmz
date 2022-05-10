from types import FunctionType
a = (x for x in [1])

a = getattr(a, "__next__")

b = getattr(iter([1, 2, 3]), "next")

aa = getattr(iter([1, 2, 3]), "close")
bb = getattr(iter([1, 2, 3]), "__iter__")

flag &= type(a) is FunctionType
flag &= type(b) is FunctionType
flag &= type(aa) is FunctionType
flag &= type(bb) is FunctionType
#
flag &= check_builtin_function_type(a, type(a()), ())
flag &= check_builtin_function_type(b, type(b()), ())
flag &= check_builtin_function_type(aa, type(aa()), ())
flag &= check_builtin_function_type(bb, type(bb()), ())

# builtin_function_or_method type

def check_builtin_function_or_method_type(actual, return_type, parameters):
    flag = True

    flag &= hasattr(actual, "__name__
