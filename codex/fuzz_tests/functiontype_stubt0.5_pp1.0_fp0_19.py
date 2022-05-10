from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_frame.f_locals)
print(type(b))
print(isinstance(b, FunctionType))

print(b())
print(b())
print(b())

print('-' * 10)


def gen():
    for i in range(5):
        yield i

g = gen()
print(g.gi_frame.f_lasti)
print(next(g))
print(g.gi_frame.f_lasti)
print(next(g))
print(g.gi_frame.f_lasti)
print(next(g))
print(g.gi_frame.f_lasti)
print(next(g))
print(g.gi_frame.f_lasti)
print(next(g))
print(g.gi_frame.f_lasti)
print(next(g))
print(
