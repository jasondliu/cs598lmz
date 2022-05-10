from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))

print(a.gi_code)
print(a.gi_frame)
print(a.gi_running)
print(a.gi_yieldfrom)

print(a.__next__())
print(a.__next__())

# print(a.__next__())

def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(dir(g))
print(g.gi_code)
print(g.gi_frame)
print(g.gi_running)
print(g.gi_yieldfrom)

print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

def gen2():
    yield from [1, 2, 3]

g2 = gen2()
print(dir(g2))
print(g2.gi_code)
