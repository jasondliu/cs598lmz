import _struct
# Test _struct.Struct
import collections
import operator
from test import test_support

def sorted(l):
    l = list(l)
    l.sort()
    return l

defs = ""
def add(fmt, *values):
    global defs
    name = "S_" + fmt.replace(" ", "_").replace("@", "")
    defs += "    %s = '%s'\n" % (name, fmt)
    for n, v in enumerate(values):
        defs += "    v%s_%s = %r\n" % (n, name, v)

# alignment
add("x", b"x")
add("=x", b"x")
add("<x", b"x")
add(">x", b"x")

# native sizes
add("c", b"x")
add("c", b"\x80")
add("b", 1)
add("b", -1)
add("b", 128)
add("b", -128)
add("B", 1)
add("B", 255)

