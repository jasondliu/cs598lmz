fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# No exception, but the code object can not be run!

# Python 2
def fn():
    return 0
fn.__code__.co_code = 'a'
fn()

# Python 3
def fn():
    return 0
fn.__code__ = 'a'
fn()
