gi = (i for i in ())
# Test gi.gi_code is not NULL
x = gi.gi_code

class A:
    def __init__(self):
        self.s = "A"
    def __len__(self):
        return 1

a = A()
a.a = a

class B(A):
    def __init__(self):
        self.s = "B"

b = B()
b.b = b

c = C()
c.c = c

try:
    i = iter(a)
    x = len(i)
except TypeError:
    print("SKIP")
    raise SystemExit

# The following must not raise a RecursionError
print(next(i), next(i), next(i), next(i))

for i in (a, b, c):
    print(i.s, len(i), list(i), next(i), next(i), next(i), next(i))

i = iter(gi)
try:
    next(i)
except StopIteration:
    print("StopIteration")
