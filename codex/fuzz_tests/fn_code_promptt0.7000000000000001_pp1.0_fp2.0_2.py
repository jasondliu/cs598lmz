fn = lambda: None
# Test fn.__code__
# This should raise an AttributeError on 3.0;
# on 2.6, it raises a TypeError, on 2.7 it raises a ValueError.
# We need to catch all three.
try:
    fn.__code__
except (AttributeError, TypeError, ValueError):
    pass
else:
    print("SKIP")
    import sys
    sys.exit()

# Test fn.__call__
# This should raise an AttributeError on 2.6 and 2.7;
# on 3.0, it raises a TypeError.
# We need to catch both.
try:
    fn.__call__
except (AttributeError, TypeError):
    pass
else:
    print("SKIP")
    import sys
    sys.exit()
