fn = lambda: None
# Test fn.__code__ and fn.__defaults__ exist
setup_fn.__code__
fn.__defaults__

# Test fn.__closure__ doesn't exist
try:
    fn.__closure__
except AttributeError:
    pass
else:
    raise Exception("fn.__closure__ should not exist!")

# Test fn.__annotations__ doesn't exist
try:
    fn.__annotations__
except AttributeError:
    pass
else:
    raise Exception("fn.__annotations__ should not exist!")

# Test fn.__kwdefaults__ doesn't exist
try:
    fn.__kwdefaults__
except AttributeError:
    pass
else:
    raise Exception("fn.__kwdefaults__ should not exist!")

# Test fn.__dict__ works
setup_fn.__dict__['x'] = 7
assert (setup_fn.x == 7)

# Test fn.__class__ works
assert (setup_fn.__class__ is types.FunctionType)

# Test fn.__code__ can be assigned
orig_code
