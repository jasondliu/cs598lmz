fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__defaults__
# Test fn.__code__.co_argcount
def fn1(spam, eggs, toast=0, ham=0):
    pass

fn = fn1
fn.__code__.co_varnames
fn.__code__.co_argcount
fn.__defaults__

# Test fn.__code__.co_flags
# Test code.co_flags & parameter
# Test code.co_flags & 0x04
# Test code.co_flags & 0x08
# Test code.co_flags & 0x20
# Test code.co_flags & 0x40
# Test code.co_flags & 0x80
# Test code.co_flags & 0x100
# Test code.co_flags & 0x400
# Test code.co_flags & 0x800
# Test code.co_flags & 0x1000
# Test code.co_flags & 0x4000
def fn2(a,b):
    print(a,b)
    
fn = fn2
fn.
