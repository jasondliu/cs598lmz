from types import FunctionType
a = (x for x in [1])
print(type(a))
b = (x for x in [1])
print(type(b))
print(a==b)

a=FunctionType(a,globals())
print(type(a))
print(a)

print(a.__code__)
print(a.__code__.co_argcount)
print(a.__code__.co_varnames)
print(a.__code__.co_name)
print(a.__code__.co_filename)
print(a.__code__.co_lnotab)
print(a.__code__.co_firstlineno)
print(a.__code__.co_flags)
print(a.__code__.co_consts)
print(a.__code__.co_names)
print(a.__code__.co_nlocals)
print(a.__code__.co_stacksize)
print(a.__code__.co_freevars)
print(a.__code__.co_cellvars)

print
