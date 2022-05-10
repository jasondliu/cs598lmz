fn = lambda: None
# Test fn.__code__.co_filename
# fn.__code__ = None
# Test fn.__closure__
# fn.__closure__ = None
# Test fn.__annotations__
# fn.__annotations__ = None
# Test fn.__primme__
# fn.__primme__ = None

# Test function type builtin construtor
def fn():
    global p
    p = Function()


fn()
del global_ns[-1]
other_fn = Function(p.__code__,p.__globals__,p.__name__,p.__defaults__, p.__closure__)
del global_ns[-1]
# Check invalid instance constructors
check_with_err(lambda: Function(666, 123, 'foo', [1,2,3], ('a', 'b')))
check_with_err(lambda: Function(p.__code__, p.__globals__, 1, p.__defaults__, p.__closure__))
check_with_err(lambda: Function(p.__code__, p.__gl
