from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, FunctionType))

print('-' * 100)

def create_num():
    for i in range(10):
        yield i

def create_num2():
    for i in range(10):
        yield i
    return '123'

def create_num3():
    for i in range(10):
        yield i
    return None

def create_num4():
    for i in range(10):
        yield i

print(type(create_num()))
print(type(create_num2()))
print(type(create_num3()))
print(type(create_num4()))

print('-' * 100)

a = create_num()
print(a)
print(type(a))
print(isinstance(a, FunctionType))
