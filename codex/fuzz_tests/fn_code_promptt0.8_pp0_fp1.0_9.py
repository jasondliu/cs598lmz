fn = lambda: None
# Test fn.__code__
test_fn.__code__ = 'a'
test_fn.__code__ = fn_with_attrs
test_fn.__code__ = fn_with_attrs.__code__
test_fn.__code__ = fn_with_attrs.__code__.replace(co_cellvars=())
# Test fn.__closure__
test_fn.__closure__ = 'a'
test_fn.__closure__ = (cell_with_attrs,)
test_fn.__closure__ = fn_with_attrs.__closure__
test_fn.__closure__ = fn_with_attrs.__closure__.replace(cell_contents=1)
# Test fn.__globals__
test_fn.__globals__ = 'a'
test_fn.__globals__ = {'b': 1}
test_fn.__globals__ = globals()
# Test fn.__dict__
test_fn.__dict__ = 'a'
test_fn.__dict__ = {'b': 1}

# Test types
