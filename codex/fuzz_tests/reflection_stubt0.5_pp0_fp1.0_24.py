fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test __code__.co_argcount

def fn(a, b, c, d, e):
    pass

try:
    fn.__code__.co_argcount = 3
except TypeError:
    print("TypeError")

# test __code__.co_consts

def fn():
    pass

try:
    fn.__code__.co_consts = (1, 2, 3, 4)
except TypeError:
    print("TypeError")

# test __code__.co_filename

def fn():
    pass

try:
    fn.__code__.co_filename = "abc"
except TypeError:
    print("TypeError")

# test __code__.co_firstlineno

def fn():
    pass

try:
    fn.__code__.co_firstlineno = 1
except TypeError:
    print("TypeError")

# test __code__.co_flags

def fn():
    pass

try:
    fn.__code__
