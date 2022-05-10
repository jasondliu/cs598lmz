fn = lambda: None
# Test fn.__code__
test_fn.__code__
test_fn.__code__.co_filename
test_fn.__code__.co_firstlineno
test_fn.__code__.co_consts
test_fn.__code__.co_argcount
test_fn.__code__.co_varnames
test_fn.__code__.co_names
test_fn.__code__.co_flags
test_fn.__code__.co_nlocals
test_fn.__code__.co_code

# Test fn.__closure__
def closure_test():
    val = 1
    def outer():
        v2 = val
        return v2
    return 1, outer.__closure__[0].cell_contents
    #return 1, v2

closure_test()

# Test fn.__annotations__
def annotate(x:'YamlisGod') -> 'YamlisGod':
    return x

annotate.__annotations__

# Test fn.__defaults__
def default(a, b=2):
   
