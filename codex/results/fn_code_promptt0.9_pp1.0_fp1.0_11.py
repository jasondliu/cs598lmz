fn = lambda: None
# Test fn.__code__.co_argcount

# Test fn.__code__.co_flags
def fn(x, *y, **z): pass
assert fn.__code__.co_flags == inspect.CO_VARARGS | inspect.CO_VARKEYWORDS
def fn(x, y=1, *z, **w): pass
assert fn.__code__.co_flags == inspect.CO_VARARGS | inspect.CO_VARKEYWORDS | inspect.CO_OPTIMIZED | inspect.CO_NEWLOCALS

# Test fn.__code__.co_firstlineno
def fn(y):
    global x
    x = 5
    print(x)
print(fn.__code__.co_firstlineno)
assert fn.__code__.co_firstlineno == 2

# Test fn.__code__.co_lnotab
print(fn.__code__.co_lnotab)
print(fn.__code__.co_firstlineno + 1, x)


#Test fn.__code__.co_closure

