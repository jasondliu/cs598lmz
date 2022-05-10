fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a regression test for a bug in the compiler.  The
# following code triggered a SystemError because of a bug in
# the handling of list comprehensions.
[(x,y) for x in range(3) for y in range(x)]

# This is a regression test for a bug in the compiler.  The
# following code triggered a SystemError because of a bug in
# the handling of list comprehensions.
[(x,y) for x in range(3) for y in range(x)]

# This is a regression test for a bug in the compiler.  The
# following code triggered a SystemError because of a bug in
# the handling of list comprehensions.
[(x,y) for x in range(3) for y in range(x)]

# This is a regression test for a bug in the compiler.  The
# following code triggered a SystemError because of a bug in
# the handling of list comprehensions.
[(x,y) for x in range(3) for y in range(x)]

# This is a regression test for a
