from types import FunctionType
a = (x for x in [1]) # A generator
isinstance(a, Iterator) # True
b = isinstance(x for x in [1],Iterator)
print(b)

# yield
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'
for char in my_generator():
    print(char)

# g = my_generator()
# print(g.__next__)
# g.__next__()
# g.__next__()
# g.__next__()

def fib(n = 1):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
for x in fib(10):
    print(x)

# coroutine
def grep(pattern):
    print('Searching for',pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)
if __name__ == '__main__':
    search = grep('coroutine')

    next(search)

