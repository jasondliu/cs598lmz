fn = lambda: None
# Test fn.__code__
expected_exception = TypeError
actual_exception = None
try:
    fn.__code__
except TypeError as e:
    actual_exception = e
assert actual_exception != None and type(actual_exception) == expected_exception # Check that function raised expected error
# Test fn.__globals__
expected_exception = TypeError
actual_exception = None
try:
    fn.__globals__
except TypeError as e:
    actual_exception = e
assert actual_exception != None and type(actual_exception) == expected_exception # Check that function raised expected error
# Test fn.__name__
expected_exception = AttributeError
actual_exception = None
try:
    fn.__name__
except AttributeError as e:
    actual_exception = e
assert actual_exception != None and type(actual_exception) == expected_exception # Check that function raised expected error
# Test fn.__defaults__
expected_exception = TypeError
actual_exception = None
try:
   
