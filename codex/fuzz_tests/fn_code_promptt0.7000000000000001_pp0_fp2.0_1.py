fn = lambda: None
# Test fn.__code__.co_varnames
for i, arg in enumerate(fn.__code__.co_varnames):
    print(i, arg)
# fn.__code__.co_argcount


# https://stackoverflow.com/a/33228068/4126114
def test(a, b, c, d):
    return d

def test2(a, b, c, d):
    return d

print(test.__code__.co_argcount)
print(test.__code__.co_varnames)
print(test.__code__.co_varnames[:test.__code__.co_argcount])

# https://stackoverflow.com/a/33228068/4126114
# Is this the same as fn.__code__.co_varnames?
def test3(a, b, c, d):
    return d

print(test3.__code__.co_varnames[:test3.__code__.co_argcount])

# https://stackoverflow.
