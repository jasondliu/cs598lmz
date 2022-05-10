gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<stdin>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<stdin>'

# Test that generator expressions are not considered as generators
assert not isinstance((i for i in ()), types.GeneratorType)

# Test that generator expressions are not considered as coroutines
assert not inspect.iscoroutine((i for i in ()))

# Test that generator expressions are not considered as coroutines
assert not inspect.isawaitable((i for i in ()))

# Test that generator expressions are not considered as coroutines
assert not inspect.isasyncgen((i for i in ()))


