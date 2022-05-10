from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a)
print(b)
print(type(a))
print(type(b))
print(isinstance(a,FunctionType))
print(isinstance(b,FunctionType))

# 测试yield
def test_yield():
    for i in range(5):
        yield i
        print('after yield',i)
    print('after for')

# 测试return
def test_return():
    for i in range(5):
        return i
        print('after return',i)
    print('after for')

# 测试yield+return
def test_yield_return():
    for i in range(5):
        yield i
        return i
        print('after yield',i)
    print('after for')

# 测试yield+return
def test_yield_return():
    for i in range(5):
        yield i
        return i
        print('after yield',i)
    print('after for')
