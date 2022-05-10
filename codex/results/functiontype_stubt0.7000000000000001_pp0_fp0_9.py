from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a)
print(b)
print(type(a))
print(type(b))
print(a)
print(b)

print(a.gi_frame)
print(b.gi_frame)

print(a.gi_frame.f_lasti)
print(b.gi_frame.f_lasti)

print(a.gi_frame.f_lasti is b.gi_frame.f_lasti)

print(a.gi_frame.f_code)
print(b.gi_frame.f_code)

print(a.gi_frame.f_code is b.gi_frame.f_code)


def func_gen():
    yield 1
    yield 2
c = func_gen()
print(c)
print(type(c))
print(type(c) == GeneratorType)
print(isinstance(c, GeneratorType))

print(type(func_gen) == FunctionType)
print(isinstance(func_gen, FunctionType))
