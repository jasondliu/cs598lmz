import types
types.new_class( "E", (object,), dict( a=1, b=2, c=3 ) )

# and this is how you instantiate it
E = types.new_class( "E", (object,), dict( a=1, b=2, c=3 ) )
e = E()
print e.a, e.b, e.c

# but this is better, so that you can set the class name too
E = types.new_class( "E", (object,), dict( a=1, b=2, c=3 ) )
e = E()
print e.a, e.b, e.c

# This is just to show what the class looks like
print E

# here's an example of inheritance
F = types.new_class( "F", (E,), dict( d=4, e=5, f=6 ) )
f = F()
print f.a, f.b, f.c, f.d, f.e, f.f

# This is just to show what the class looks like
print F

