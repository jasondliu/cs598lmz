fn = lambda: None
# Test fn.__code__ == fn.__code__
assert fn.__code__ == fn.__code__
# Test fn.__code__ is not fn.__code__
assert fn.__code__ is not fn.__code__
# Test fn.__globals__ == fn.__globals__
assert fn.__globals__ == fn.__globals__
# Test fn.__globals__ is not fn.__globals__
assert fn.__globals__ is not fn.__globals__
# Test fn.__defaults__ == fn.__defaults__
assert fn.__defaults__ == fn.__defaults__
# Test fn.__defaults__ is not fn.__defaults__
assert fn.__defaults__ is not fn.__defaults__
# Test fn.__closure__ == fn.__closure__
assert fn.__closure__ == fn.__closure__
# Test fn.__closure__ is not fn.__closure__
assert fn.__closure__ is not fn.__closure__
# Test fn.__kwdefaults__ == fn.__kw
