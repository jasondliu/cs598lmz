from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(type(a)))
b = FunctionType(a, globals(), 'my_gen')
print(b)
print(type(b))
print(type(type(b)))
print(b.__code__.co_argcount)
print(b.__code__.co_code)
c = b(4)
print(c)
print(type(c))
print(type(type(c)))
print(c.__code__.co_argcount)
print(c.__code__.co_code)

print('-------------------')

def test(n):
    return (i for i in range(n))

b = test(5)
print(b)
print(type(b))
print(type(type(b)))
print(b.__code__.co_argcount)
print(b.__code__.co_code)
c = b(4)
print(c)
print(type(c))
print(type(type(c)))
print(c.__code__.co
