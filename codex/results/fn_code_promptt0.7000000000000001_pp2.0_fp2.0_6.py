fn = lambda: None
# Test fn.__code__ attribute
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

print(fn.__code__.co_filename)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_name)

def fn():
    pass

print(fn.__code__.co_filename)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_name)

print(fn.__code__.co_code.hex())
print(fn.__code__.co_consts)
print(fn.__code__.co_varnames)
print(fn.__code__.co_freevars)
print(fn.__code__.co_cellvars)

try:
    eval(fn.__code__)
except TypeError:
    print('TypeError')
