fn = lambda: None
# Test fn.__code__
test_fn.__code__ = 42
test_fn = smc_eval("test_fn", locals(), {"test_fn" : test_fn} )
print test_fn.__code__
if test_fn.__code__ is 42:
    test_fn.__code__ = test_fn_code
else:
    test_fn.__code__ = 42
    test_fn = smc_eval("test_fn", locals(), {"test_fn" : test_fn} )
    test_fn.__code__ = test_fn_code
test_fn()

test_fn2 = 42
test_fn2 = smc_eval("test_fn2", locals(), {"test_fn2" : test_fn2})
print test_fn2
if test_fn2 is 42:
    test_fn2 = test_fn
else:
    test_fn2 = 42
    test_fn2 = smc_eval("test_fn2", locals(), {"test_fn2" : test_fn2})
    test_fn2 = test_fn
test_fn2
