from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))
print(isinstance(a,GeneratorType))

def fibonacci(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        yield a
        a,b = b,a+b
        count += 1
    return 'done'

def test():
    for i in fibonacci(10):
        print(i)

test()
