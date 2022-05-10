fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

# __code__ must be a code object
fn = lambda: None
fn.__code__ = 42
try:
    fn()
except TypeError as e:
    print(e)

# __code__ must be a code object
fn = lambda: None
fn.__code__ = "abc"
try:
    fn()
except TypeError as e:
    print(e)

# __code__ must be a code object
fn = lambda: None
fn.__code__ = {}
try:
    fn()
except TypeError as e:
    print(e)

# __code__ must be a code object
fn = lambda: None
fn.__code__ = []
try:
    fn()
except TypeError as e:
    print(e)

# __code__ must be a code object
fn = lambda: None
fn.__code__ = ()
try:
    fn()
except TypeError as e:
    print(e)

# __code__
