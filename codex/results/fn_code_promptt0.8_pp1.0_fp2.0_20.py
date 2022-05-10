fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
# Test fn.__code__.co_argcount
fn.__code__.co_argcount
# Test fn.__code__.co_code
fn.__code__.co_code
# Another test of fn.__code__.co_code
fn.__code__.co_code
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize
# Test fn.__code__.co_flags
fn.__code__.co_flags
# Test the co_flags attribute in a module scope
def fn(x, y, z):
    return x + y + z
fn.__code__.co_flags
# Test the co_flags attribute in a class scope
class C(object):
    def fn(self, x, y, z):
        return x + y + z
    property(fn, None)
C.fn.__code__.co_flags
# Test fn.__code__.co_consts
def fn(x, y
