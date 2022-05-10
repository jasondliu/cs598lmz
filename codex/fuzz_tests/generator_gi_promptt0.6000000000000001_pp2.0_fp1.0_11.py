gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise Exception("AttributeError should be raised")
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    raise Exception("AttributeError should be raised")
# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    raise Exception("AttributeError should be raised")
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    raise Exception("AttributeError should be raised")

def fg():
    yield from (i for i in ())

fg = fg()
# Test fg.gi_code
try:
    fg.gi_code
except AttributeError:
    pass
else:
    raise Exception("AttributeError should be raised")
# Test fg.gi_frame
try:
    fg.gi_frame
except
