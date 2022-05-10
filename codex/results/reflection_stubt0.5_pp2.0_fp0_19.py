fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError:
    pass
else:
    print('FAILED: __code__ = generator')

# Test __code__ = memoryview

fn = lambda: None
mv = memoryview(b"")
fn.__code__ = mv

try:
    fn()
except TypeError:
    pass
else:
    print('FAILED: __code__ = memoryview')

# Test __code__ = type

fn = lambda: None
fn.__code__ = type

try:
    fn()
except TypeError:
    pass
else:
    print('FAILED: __code__ = type')

# Test __code__ = str

fn = lambda: None
fn.__code__ = "abc"

try:
    fn()
except TypeError:
    pass
else:
    print('FAILED: __code__ = str')

# Test __code__ = bytes

fn = lambda: None
fn.__code__ = b"abc"

try:
    fn
