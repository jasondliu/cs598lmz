import types
types.MethodType(coerce, None, type)

# This shouldn't work yet, because __coerce__ isn't implemented
# for strings.  If we get past this, the coercion is successful. 
# Call the coercion, check the result.
s = coerce(None, "a")

# Make sure we got the right types back. 
