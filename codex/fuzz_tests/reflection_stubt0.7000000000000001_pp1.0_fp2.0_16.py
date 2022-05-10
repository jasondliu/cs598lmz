fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

print("List comprehension:")
a = [i for i in range(0, 100)]
print("a =", a)

print("Generator comprehension:")
b = (i for i in range(0, 100))
print("b =", b)

print("List comprehension is faster:")
%timeit a = [i for i in range(0, 1000)]
%timeit b = (i for i in range(0, 1000))

print("Iterate through list:")
for i in a:
    pass

print("Iterate through generator:")
g = (i for i in range(0, 100))
for i in g:
    pass


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci numbers generator:")
for i in fibonacci(100):
    print(i, end=" ")

print("\n\n")

import collections

Point = collections.
