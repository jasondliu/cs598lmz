fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as exc:
    print(exc)

print(fn.__code__)

# The __code__ attribute of a function is a writable descriptor.
# So it is possible to assign an arbitrary object to it
# when it is not a code object.
# But it will be turned back automatically to a code object when
# the function is called.

print()
fn = lambda: None
fn.__code__ = [1, 2, 3, 4]
try:
    fn()
except TypeError as exc:
    print(exc)

print(fn.__code__)
