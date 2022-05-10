from types import FunctionType
list(FunctionType(lambda: 0, {}, None, None, None).__code__.co_varnames)

# %%
def f1(a, b, c):
    return a + b + c

def f2(a, b, c, d):
    return a + b + c + d

def f3(a, b, c, d, e):
    return a + b + c + d + e

# %%
def f1_factory(a, b, c):
    def f1(d):
        return a + b + c + d
    return f1

def f2_factory(a, b, c, d):
    def f2(e):
        return a + b + c + d + e
    return f2

def f3_factory(a, b, c, d, e):
    def f3(f):
        return a + b + c + d + e + f
    return f3

# %%
def f1_factory(a, b, c):
    def f1(d, e, f
