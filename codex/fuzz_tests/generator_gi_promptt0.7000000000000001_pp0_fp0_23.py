gi = (i for i in ())
# Test gi.gi_code does not exist.
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")
