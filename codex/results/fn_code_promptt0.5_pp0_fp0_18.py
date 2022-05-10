fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('x', 'y')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_argcount
# fn.__code__.co_argcount = 3

# Test fn.__code__.co_argcount
@dataclass
class Foo:
    x: int
    y: str

# Test fn.__code__.co_argcount
def bar(x: int, y: str):
    pass

# Test fn.__code__.co_argcount
def baz(x: int, y: str = 'y') -> int:
    return x + len(y)

# Test fn.__code__.co_varnames
def quux(x: int, y: str = 'y') -> int:
    x += 1
    y += 'z'
    return x + len(y)

# Test fn.__code__.co_varnames
def qu
