fn = lambda: None
# Test fn.__code__.co_argcount
Test.assert_equals(fn.__code__.co_argcount, 0)


import string
# Test that .isalpha() returns True for ''.join(letters)
letters = [l for l in string.ascii_lowercase]
Test.assert_equals([c.isalpha() for c in letters], [True] * 26)
