gi = (i for i in ())
# Test gi.gi_code.co_name
gi.gi_code.co_name

# Test missing attribute for SF bug #1517084
try:
    None.x
except AttributeError:
    pass

# Test missing attribute for SF bug #1517084
try:
    "".x
except AttributeError:
    pass

# Test missing co_names for SF bug #1573348
try:
    tmp = None.x
except AttributeError:
    pass

# Test handling of missing co_names for SF bug #1573348
def f():
    def g():
        pass
    g.func_code = None
    return g
f()()

# Test missing co_filename for SF bug #1573406
import sys
try:
    tmp = sys.path.x
except AttributeError:
    pass

# Test handling of missing co_filename for SF bug #1573406
def f():
    def g():
        pass
    g.func_code = type(g.func_code)(0, 0, 0, 0, "", "", (), (), (),
