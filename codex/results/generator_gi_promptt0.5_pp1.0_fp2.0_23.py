gi = (i for i in ())
# Test gi.gi_code is None
print("gi.gi_code is %s" % gi.gi_code)

# Test gi.gi_frame is None
print("gi.gi_frame is %s" % gi.gi_frame)

# Test gi.gi_running is False
print("gi.gi_running is %s" % gi.gi_running)

# Test gi.gi_yieldfrom is None
print("gi.gi_yieldfrom is %s" % gi.gi_yieldfrom)

# Test gi.__name__ is 'gi'
print("gi.__name__ is %s" % gi.__name__)

# Test gi.__qualname__ is 'gi'
print("gi.__qualname__ is %s" % gi.__qualname__)

# Test gi.__module__ is '__main__'
print("gi.__module__ is %s" % gi.__module__)

# Test gi.__class__ is <class 'generator'>
print("gi.__class
