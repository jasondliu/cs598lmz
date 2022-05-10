from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda")(1))

FunctionType(lambda x: x, globals(), "lambda")(1)

class Foo:
    def __call__(self, x):
        return x

foo = Foo()
foo(1)

class Bar(Foo):
    pass

bar = Bar()
bar(1)

class Foo:
    def spam(self, x):
        print("spam")
        x(42)

class Bar:
    def __init__(self):
        self.x = 42

foo = Foo()
foo.spam(lambda: print(bar.x))

def outer():
    x = 42
    def inner():
        print(x)
    inner()

outer()

def outer():
    x = 42
    def inner():
        print(x)
    return inner

fn = outer()
fn()

def outer():
    x = 42
    def inner():
        print(x)
    return inner

outer()()

def outer():
    x
