fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
ret = func(fn)
assert ret.__class__ == str
assert func.__annotations__ == {'fn': FunctionType}

# Check that annotations are preserved for decorated functions

def dec1(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

def dec2(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@dec1
@dec2
def sub(i: int) -> int:
    return i - 1

assert sub.__annotations__ == {'i': int, 'return': int}
assert sub.__wrapped__.__annotations__ == {'i': int, 'return': int}

# Check that the signature of a class method is preserved (and not
# the signature of the class)

def dec(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

class C:
    @dec
