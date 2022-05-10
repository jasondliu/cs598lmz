fn = lambda: None
# Test fn.__code__ and fn.__closure__
def test_fn(arg):
    return arg

print(test_fn.__code__)

print(test_fn.__code__.co_argcount)

print(test_fn.__code__.co_varnames)

print(test_fn.__code__.co_freevars)

print(test_fn.__closure__)

print(test_fn.__code__.co_consts)


# Test fn.func_closure and fn.func_code
def test_fn(arg):
    return arg

print(test_fn.func_closure)

print(test_fn.func_code)

print(test_fn.func_code.co_argcount)

print(test_fn.func_code.co_varnames)

print(test_fn.func_code.co_freevars)

print(test_fn.func_closure)

print(test_fn.func_code.co_consts)
