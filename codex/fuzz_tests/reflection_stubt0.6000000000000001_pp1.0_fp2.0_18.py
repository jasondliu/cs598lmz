fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    print("TypeError")

# __code__ = ''
try:
    exec("def fn(): pass\nfn.__code__ = ''\nfn()")
except TypeError:
    print("TypeError")

# __code__ = int
fn = lambda: None
fn.__code__ = 1
try:
    fn()
except TypeError:
    print("TypeError")

# __code__ = 0.0
fn = lambda: None
fn.__code__ = 0.0
try:
    fn()
except TypeError:
    print("TypeError")

# __code__ = None
fn = lambda: None
fn.__code__ = None
try:
    fn()
except TypeError:
    print("TypeError")

# __code__ = float('nan')
fn = lambda: None
fn.__code__ = float('nan')
try:
    fn()
except TypeError:
    print("TypeError")

# __code__ = float('inf')
fn = lambda
