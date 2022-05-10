fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename
"""

def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

nf1(1)
nf2(1)

#nf1.__closure__
#nf1.__closure__[0].cell_contents

#nf2.__closure__
#nf2.__closure__[0].cell_contents

def repeat(str):
    def times(num):
        return str * num
    return times

r1 = repeat("hello")
r2 = repeat("goodbye")

r1(2)
r2(2)
r1(3)

def outer():
    x = "foo"
    def inner():
        x = "bar"
    inner()
    return x

outer()

def outer():
    x = "foo"
    def inner():
        nonlocal x
        x = "bar"

