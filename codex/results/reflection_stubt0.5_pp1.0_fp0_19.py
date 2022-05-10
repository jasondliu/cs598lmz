fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()

# gi is not a code object, so a TypeError should be raised
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# A code object with a non-tuple co_code should raise a TypeError
class A:
    def __init__(self):
        self.co_code = 'x'

fn.__code__ = A()
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# A code object with a tuple co_code but a non-integer co_firstlineno
# should raise a TypeError
class A:
    def __init__(self):
        self.co_code = ()
        self.co_firstlineno = 'x'

fn.__code__ = A()
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# A code object with a tuple co_code but a non-integer co_
