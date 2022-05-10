fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Function names
test_data = [
    (fn, '<lambda>'),
    (type, 'type'),
    (type(lambda: None), 'function'),
    (int, 'int'),
]

# Test.
for func, expected_name in test_data:
    print(func_name(func), ' == ', expected_name, ' ? ',
          func_name(func) == expected_name)
