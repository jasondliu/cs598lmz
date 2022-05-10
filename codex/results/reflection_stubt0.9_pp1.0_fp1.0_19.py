fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi # Throws and AttributeError, which is what we wanted to catch.

try:
    fn()
    did_throw = False
except (IOError, AttributeError, Exception):
    did_throw = True

assert did_throw
 
# filename must have the same format of __file__ variable
try:
    fn.__code__ = 'spam, spam'
    fn.__code__.co_filename #__txt, ___literalAttribute
    did_throw = False
except AttributeError:
    did_throw = True
assert did_throw

def baz():
    pass
assert baz.__code__.co_filename.endswith('__pyscript__')
assert baz.__code__.co_firstlineno == 2

# Creates a script
def f():
    x = 2
    return x
assert f.__code__.co_filename.endswith('__pyscript__')
assert f.__code__.co_firstlineno == 1
 
# Creates a script
def f():
    return lambda
