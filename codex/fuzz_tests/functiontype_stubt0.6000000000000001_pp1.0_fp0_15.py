from types import FunctionType
a = (x for x in [1])
print(a)

a = (x for x in [1,2,3])
print(a)

print(next(a))
print(next(a))
print(next(a))
# print(next(a)) # StopIteration

def mygen():
    yield 1
    yield 2

mya = mygen()
print(next(mya))
print(next(mya))

b = [x**2 for x in [1, 2, 3, 4, 5]]
print(b)

c = (x**2 for x in [1, 2, 3, 4, 5])
print(c)

print(next(c))
print(next(c))
print(next(c))

for x in c:
    print(x)

def mygen2(n):
    while n > 0:
        yield n
        n -= 1

mya = mygen2(5)
print(next(mya))
print(next(mya))
print(next(mya))

for x in mya:
