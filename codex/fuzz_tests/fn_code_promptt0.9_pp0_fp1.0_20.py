fn = lambda: None
# Test fn.__code__ is None (will be false if the user has set __code__ to None)
_test_fn.__code__ = False
mock_obj = Mock()
mock_obj.method.__code__ = False

assert_in(
    '.'.join([
        'Specify the exact return_value of a mock',
        'in order to help with dynamic mocking'
    ]),
    assert_msg('specify the return_value of a mock', mock_obj.method),
)
assert_in(
    'Unknown attribute of',
    assert_msg('specify the return_value of a mock', _test_fn.__code__),
)
assert_in(
    "Unknown attribute of",
    assert_msg("specify the return_value of a mock", _test_fn),
)

# Test for string references in assert messages
if not PY3:
    string_value = ''.encode(sys.getdefaultencoding())
else:
    string_value = ''
assert_in("string object", assert_msg("string", string_value))
assert_
