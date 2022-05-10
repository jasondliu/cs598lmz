from types import FunctionType
a = (x for x in [1])
b = (lambda: 2)
print(type(a))
print(type(b))
print("isinstance(a, FunctionType):", isinstance(a, FunctionType))
print("isinstance(a, GeneratorType):", isinstance(a, GeneratorType))
print("isinstance(b, FunctionType):", isinstance(b, FunctionType))
print("isinstance(b, GeneratorType):", isinstance(b, GeneratorType))

print("\n----------------------\n")


def foo():
    for _ in range(4):
        x = 1
        yield x
        x = 2


def bar():
    x = 1
    yield x
    x = 2


print("\n Function foo:")
foo_gen = foo()
print("type(foo):", type(foo))
for i in range(3):
    print("next(foo_gen):", next(foo_gen))
for _ in range(3):
    print("next(foo_gen):", next(foo_gen))


bar_gen = bar()
for _ in range(3):
