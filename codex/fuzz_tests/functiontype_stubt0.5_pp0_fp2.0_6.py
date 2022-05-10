from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def test():
    yield 1

b = test()
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print(dir(a))
print(dir(b))

print(b.gi_code)
print(b.gi_frame.f_lasti)
print(b.gi_frame.f_locals)
print(b.gi_frame.f_back)

print(a.gi_code)
print(a.gi_frame.f_lasti)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_back)


def test2(x):
    yield x

c = test2(1)
print(c.gi_code)
print(c.gi_frame.f_lasti)
print(c.gi_frame.f_locals)
print(c.gi_frame.f_back)


def test3(x):
