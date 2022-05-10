gi = (i for i in ())
# Test gi.gi_code.co_filename

# On Windows, PyArg_ParseTuple can't handle a unicode object with embedded NULLs --
# it just chokes.
#
# This test asserts that this case is properly handled and that the exception
# raised is a TypeError.

def func(a): pass
u = unicode("abc\0def", "utf-8")

try:
    func(u)
except TypeError:
    pass
else:
    print "expected a TypeError"

if u"\x00" in u:
    print "Wrong string!"
