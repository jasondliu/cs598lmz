from types import FunctionType
a = (x for x in [1])
b = (1 for x in [1])
d = a.send('b')
print(d, '\n')
d = a.send(None)
print(d)
print(type(a))
print(type(b))
print(type({}))
print(type([]))
print(type(()))
print(type(0))
print(type(None))
print(type('a'))
print(type(abs))
print(type(list))
print(type(str))
print(type(int))
print(type(FunctionType))


def diff_return_value():
    print('return')
    return


print(diff_return_value(), 'type', type(diff_return_value()))


def diff_yield_value():
    yield 1
    print('return')
    return


print(diff_yield_value(), 'type', type(diff_yield_value()))
print(tuple(diff_yield_value()), 'type', type(tuple(diff_yield_value())), 't
