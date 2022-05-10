fn = lambda: None
# Test fn.__code__
# Check that the two function with different defaults have different signatures.
test_fn.__code__ = co
assert get_function_signature(test_fn) == "test_fn(*args, **kwargs)"
test_fn.__code__ = co_a
assert get_function_signature(test_fn) == "test_fn(a=5, *args, **kwargs)"
test_fn.__code__ = co_ab
assert get_function_signature(test_fn) == "test_fn(a=5, b=7, *args, **kwargs)"
# Now add in 'self' and check we get the class method behaviour as expected.
test_fn.__code__ = co
test_fn.__self__ = MyClass()
signature = get_function_signature(test_fn)
assert signature.startswith("MyClass.test_fn(*args, **kwargs)")
assert " <instance of " in signature
if hasattr(types, 'MethWrapperType'):
    # Also test with a function that's already wrapped in a MethWra
