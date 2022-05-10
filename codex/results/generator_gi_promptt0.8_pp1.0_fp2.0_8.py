gi = (i for i in ())
# Test gi.gi_code.co_stacksize.
gi.gi_code.co_stacksize == CO_MAXBLOCKS * 5

gi = (i for i in ())
# Don't set to a bad value
try:
    gi.gi_code.co_stacksize = sys.maxsize
except OverflowError:
    pass
else:
    raise Exception("Should have raised OverflowError")

gi = (i for i in ())
# Don't set to a bad value
try:
    gi.gi_code.co_stacksize = -1
except ValueError:
    pass
else:
    raise Exception("Should have raised ValueError")

# Attribute assignment allowed for code objects
co = gi.gi_code
co.co_stacksize = CO_MAXBLOCKS * 4
gi.gi_code = co
gi.gi_code.co_stacksize == CO_MAXBLOCKS * 4
