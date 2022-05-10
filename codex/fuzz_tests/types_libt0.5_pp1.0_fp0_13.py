import types
types.MethodType(lambda self: 42, None)

# E0211: No value passed for parameter '%s' in function call
# E0212: Not enough arguments for format string
def func(x, y):
    print("%s, %s" % x)
    print("%s, %s" % (x,))
    print("%s, %s" % (x, y, z))  # [no-value-for-parameter]
    print("%s, %s" % (x, y))
    print("%s, %s" % ())  # [not-enough-values-to-unpack]

# E0213: Method should have "self" as first argument
# E0236: Unknown argument name "%s" in function call
# E0237: Missing argument name "%s" in function call
# E0238: Positional argument follows keyword argument
# E0239: Function doesn't have an argument named "%s"
# E0240: %s argument after *args
# E0241: %s argument after **kwargs
# E0242: %
