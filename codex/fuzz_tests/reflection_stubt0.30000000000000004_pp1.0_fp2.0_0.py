fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = "a"
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = b"a"
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = bytearray(b"a")
except TypeError:
   
