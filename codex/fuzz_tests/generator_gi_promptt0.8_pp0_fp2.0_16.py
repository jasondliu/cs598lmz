gi = (i for i in ())
# Test gi.gi_code is None
try:
    print(gi.gi_running)
    print(gi.gi_yieldfrom)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_yieldfrom is None
class A:
    def __iter__(self):
        yield 1

a = A()
gi = (i for i in a)
print(gi.gi_running)
print(gi.gi_yieldfrom)
print(next(gi))
try:
    print(gi.gi_running)
    print(gi.gi_yieldfrom)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_yieldfrom is not None
class A:
    def __iter__(self):
        print("iter")
        yield 1

class B(A):
    def __iter__(self):
        print("super iter")
        yield from super().__iter__()

b = B()
gi = (i for i in b)
print(gi.gi
