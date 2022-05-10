fn = lambda: None
# Test fn.__code__
if hasattr(fn.__code__, 'co_code'):
    for c in fn.__code__.co_code:
        assert c in bytes(range(256))
if hasattr(fn.__code__, 'co_names'):
    for c in fn.__code__.co_names:
        assert c in str(range(256))

# This test should be in test_types
s = "this is a string"
assert s.upper() == "THIS IS A STRING"

# This test should be in test_list.py
# test list constructor
assert list("xyz") == ['x', 'y', 'z']
assert list(()) == []
assert list((1,)) == [1]
assert list((1, 2)) == [1, 2]
assert list((1, 2, 3)) == [1, 2, 3]
assert list([1, 2, 3]) == [1, 2, 3]
assert list([]) == []
assert list(range(3)) == [0, 1, 2]
assert list(range(1, 5
