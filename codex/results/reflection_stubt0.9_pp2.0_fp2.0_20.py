fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Invalid arguments
def f(): raise TestError()
Compile(f)

# Function has __code__, but __code__ is invalid
def f(): pass
def f2(): raise TestError()
f.__code__ = f2

c = Compile(f)
if c != f.__code__.__code__:
    raise TestError()

# Function is callable, but has no __code__
def f3(): raise TestError()

class C:
    def __call__(self):
        return 0

print(Compile(f3.__code__))
print(Compile(f3).__code__)
print(Compile(C()))
print(Compile(C()).__code__)

# Different code object
def f4(): return 0

print(Compile(f4))
print(Compile(f4.__code__))

c = Compile(f4.__code__)
c.co_filename = 'fffff'
Compile(c)
