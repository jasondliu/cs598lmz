from types import FunctionType
list(FunctionType("a", globals(), "", (), (), 0, None).__code__.co_varnames)

# Here is a good example of the power of the Python language:
class C:
    def f(self):
        return "f"

c = C()
print(c.f())
C.f = lambda self: "g"
print(c.f())

# This is not possible in Java:
def f(x):
    return x+1

g = f
print(g(1))

def h(x, f=f):
    return f(x)

print(h(1))

def f(x):
    return x+2

print(h(1))

print(g(1))

f = lambda x: x+3

print(h(1))

print(g(1))

# Here is another example:
def f():
    def f2():
        return "f2"
    return f2

print(f()())

def g():
    def g2():
        return "g
