fn = lambda: None
# Test fn.__code__ and fn.__globals__.items() and fn.__closure__ works.
fn2 = curry(fn)

class Foo:
    def __init__(self):
        self.x = 10
        self.y = 20
    def add(self, y):
        return self.x + y
foo = Foo()
bar = curry(foo.add, y=30)
print(bar())
assert bar() == 40

bar = curry(foo.add, 30)
print(bar())
assert bar() == 40

bar = curry(foo.add)
print(bar(40))
assert bar(40) == 50

def f(x=42): return x
assert curry(f)() == 42

f = lambda x,y,z=1: x+y+z
assert curry(f)(1)(2) == 4

'''
x = int("3")
print(x)
y = int("FF", 16)
print(y)
assert(int("3") == int("3", 10))
assert(int("3", 3) == int("
