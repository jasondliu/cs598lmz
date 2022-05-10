gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code not defined (test failed)")
try:
    gi.gi_code = 1
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code is writeable")
gi.gi_code = 0
gi.gi_code = -1
gi.gi_code = sys.maxint
gi.gi_code = -sys.maxint-1
try:
    gi.gi_code += 1
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code can be incremented")
try:
    gi.gi_code -= 1
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code can be decremented")
try:
    gi.gi_code += 1.0
except AttributeError:
    pass
else:
    raise TestFailed("gi.gi_code can be incremented")
try
