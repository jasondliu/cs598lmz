fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# {__next__: None, __self__: <generator object <lambda> at 0x10968ff88>}
print(fn.__code__)

# SF bug#1183669: __class__ assignment not allowed for some builtin types

def raise_for_non_extensible(obj):
    d = {}
    try:
        d.update(**{1: 5, -2: 7})
        d.update(**{-2: -7})  # Add another key with the same hash
        obj.__class__ = d     # Verify that we can't change a builtin's class
    except TypeError:
        return True
    else:
        return False

# Change allowed
obj = []
print(raise_for_non_extensible(obj))

# Change not allowed
obj = Exception
print(raise_for_non_extensible(obj))

# Change allowed
obj = StopIteration
print(raise_for_non_extensible(obj))

# Change allowed
obj = NotImplemented
print(raise_for_
