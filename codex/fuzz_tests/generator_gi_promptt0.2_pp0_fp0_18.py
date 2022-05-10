gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.__name__ is 'generator'
print(gi.__name__)
# Test gi.__qualname__ is '<genexpr>'
print(gi.__qualname__)
# Test gi.__module__ is '__main__'
print(gi.__module__)
# Test gi.__class__ is <class 'generator'>
print(gi.__class__)
# Test gi.__dict__ is {}
print(gi.__dict__)
# Test gi.__code__ is <code object <genexpr> at 0x7f8e9c0d7c70, file "generator.py", line 5>
print(gi.__code__)
# Test gi.__doc__
