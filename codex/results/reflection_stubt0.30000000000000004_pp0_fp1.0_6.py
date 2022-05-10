fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't create a code object with a non-code object
# as the first argument
try:
    code(gi, (), (), (), "", "", 0, b"")
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a code object with a non-tuple as the second
# argument
try:
    code(fn.__code__, "", (), (), "", "", 0, b"")
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a code object with a non-tuple as the third
# argument
try:
    code(fn.__code__, (), "", (), "", "", 0, b"")
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a code object with a non-tuple as the fourth
# argument
try:
    code(fn.__code__, (), (), "", "", "", 0, b
