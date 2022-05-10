fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn as a decorator
@fn
def deco_fn(): pass
# Test fn.__gec-closure__ property
# Test str() type
str('test')
# Test str as a decorator
@str
def deco_str(): pass
# Test len() type
len('test')
# Test len as a decorator
@len
def deco_len(): pass
# Test bool() type
bool(True)
# Test bool as a decorator
@bool
def deco_bool(): pass
# Test float() type
float(1.0)
# Test float as a decorator
@float
def deco_float(): pass
# Test float.__doc__
float.__doc__ + float.__doc__
# Test int() type
int(1)
# Test int as a decorator
@int
def deco_int(): pass
# Test int.__doc__
int.__doc__ + int.__doc__
# Test property() type
property(None)
# Test property as a decorator
@property
def deco
