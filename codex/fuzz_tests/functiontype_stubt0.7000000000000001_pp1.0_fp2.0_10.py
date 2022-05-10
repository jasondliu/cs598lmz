from types import FunctionType
a = (x for x in [1])
a

isinstance(a, FunctionType)

def test_generator():
    for i in range(10):
        yield i

a = test_generator()

print(type(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())

dir(a)


def my_generator():
    print('inside my generator')
    print('yielding 1')
    yield 1
    print('yielding 2')
    yield 2

gen = my_generator()
print(type(gen))

gen.__next__()
gen.__next__()
gen.__next__()
