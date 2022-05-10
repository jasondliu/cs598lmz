fn = lambda: None
# Test fn.__code__ works
print(fn.__code__)
# Test fn.__code__.co_code works
print(fn.__code__.co_code)
# Test fn.__code__.co_varnames works
print(fn.__code__.co_varnames)
