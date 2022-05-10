fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This is a test for a bug in the bytecode evaluation loop.
# The bug was that the top of the block stack was not cleared
# when an exception was set.  This caused a segfault when an
# (unrelated) finally clause was executed after the exception
# was set.
def f():
    try:
        1/0
    finally:
        str(__builtins__)

try:
    f()
except ZeroDivisionError:
    pass


# Check that the SET_LINENO bytecode resets the lasti value
# correctly.  This is important for tracebacks.
def f():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t =
