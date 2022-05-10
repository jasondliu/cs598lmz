fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_*
print(fn.__code__.co_argcount)
print(fn.__code__.co_stacksize)
print(fn.__code__.co_flags)
print(fn.__code__.co_code)
print(fn.__code__.co_consts)
print(fn.__code__.co_names)
print(fn.__code__.co_varnames)
print(fn.__code__.co_filename)
print(fn.__code__.co_name)
# Test fn.__code__.co_lnotab
print(fn.__code__.co_lnotab)
