from types import FunctionType
a = (x for x in [1])

b = (x for x in [2])


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for index, value in enumerate(fib()):
    if index > 10:
        print("over")
        break
    print(value)
