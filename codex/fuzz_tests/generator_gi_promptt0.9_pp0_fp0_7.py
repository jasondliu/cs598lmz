gi = (i for i in ())
# Test gi.gi_code
test_support.test_codeop(gi.gi_code, '0|0', 0, 0)


# Test code op on function code
def fn():
    pass
# Test fn.__code__.co_code
test_support.test_codeop(fn.__code__.co_code, '2|1', fn.__code__.co_argcount,
                         fn.__code__.co_nlocals)

# Test code op on generator
def gen():
    yield 42
cg = gen()
cg.next()
# Test cg.gi_code.co_code
test_support.test_codeop(cg.gi_code.co_code, '2|1', cg.gi_code.co_argcount,
                         cg.gi_code.co_nlocals)

# test __code__ default
def foo(): pass
def bar(): pass
bar.__code__ = foo.__code__
test_support.test_codeop(bar.__code__.co_code, '2|1', bar.__
