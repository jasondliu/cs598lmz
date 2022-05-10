fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# crash from a call to __new__ that is not properly handled
# in the case of an exception.
class A(object):
    def __reduce__(self):
        raise Exception
A()

# bug in the handling of the start index of a slice
# (negative numbers were handled incorrectly)
a = range(10)
a[-1:1:-1]
a[-1:1:-2]
a[-1:1:2]
a[1:-1:-1]
a[1:-1:-2]
a[1:-1:2]

# bug in the handling of the start index of a slice
# (negative numbers were handled incorrectly)
a = range(10)
a[-1:1:-1]
a[-1:1:-2]
a[-1:1:2]
a[1:-1:-1]
a[1:-1:-2]
a[1:-1:2]

# bug in the handling of the start index of a slice
# (negative numbers were handled incorrectly)
a = range(
