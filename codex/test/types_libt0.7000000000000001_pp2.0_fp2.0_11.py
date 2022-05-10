import types
types.new_class( "E", (object,), dict( a=1, b=2, c=3 ) )

# and this is how you instantiate it
E = types.new_class( "E", (object,), dict( a=1, b=2, c=3 ) )
e = E()
