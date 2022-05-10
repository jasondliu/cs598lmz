from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a))
print(type(b))
print(a==b)
print(a is b)
c = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals, a.gi_frame.f_code.co_name, a.gi_frame.f_locals)
print(c)
print(c())
print(c())
print(c())
print(c())

def add(a, b):
    return a+b

print(add(3, 4))

a = (x for x in [3, 4])
b = (x for x in [3, 4])
c = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals, a.gi_frame.f_code.co_name, a.gi_frame.f_locals)
print(c)
print(c())
print(c())
print(c())
print(c())
'''
