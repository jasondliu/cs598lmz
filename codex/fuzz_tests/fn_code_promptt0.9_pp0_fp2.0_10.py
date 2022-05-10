fn = lambda: None
# Test fn.__code__.__freevars__ and fn.__code__.co_freevars

co = fn.__code__
print(co.co_argcount)

# 3.3
# Test fn.__closure__ and fn.__code__.co_cellvars

co = fn.__code__
print(co.co_argcount)
