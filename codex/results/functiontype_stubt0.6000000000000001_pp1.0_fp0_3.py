from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(a) == type(b))
print(callable(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

print((x for x in [1]) == (x for x in [1]))
print(type(x for x in [1]))
print(isinstance(x for x in [1], GeneratorType))
print(isinstance(x for x in [1], FunctionType))

print(isinstance(x for x in [1], (FunctionType, GeneratorType)))

print(type(x for x in [1]) == type(x for x in [1]))
'''

'''
# yield
def test():
    print('func body')
    yield 1
    print('func end')

t = test()
print(t)
print(next(t))
print('-'*10)
print(next(t))
'''

''
