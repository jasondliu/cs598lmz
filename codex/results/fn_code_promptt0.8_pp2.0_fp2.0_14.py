fn = lambda: None
# Test fn.__code__.co_varnames
print(fn.__code__.co_varnames)
# Test dir(fn)
dir(fn)

# Test fn.__closure__, fn.__code__.co_freevars, fn.__code__.co_consts
def closure_test():
    def fn(x):
        def bar(y):
            return x + y
        return bar
    return fn(1)


closure = closure_test()
print(closure.__closure__)
print(closure.__code__.co_freevars)
print(closure.__code__.co_consts)

# Test fn.__closure__, dir(fn), fn.__code__.co_freevars, fn.__code__.co_consts
def closure_test():
    def fn(x):
        def bar(y):
            return x + y
        return bar
    return fn(1)

closure = closure_test()
print(closure.__closure__)
dir(closure)
print(closure.__code__.co_free
