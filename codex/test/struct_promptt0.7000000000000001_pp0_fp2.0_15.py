import _struct
# Test _struct.Struct

def test_struct_error_messages():
    # SF bug #722689 -- struct.error messages are bad
    try:
        _struct.Struct('abc')
    except _struct.error as msg:
        # The exact error message is not guaranteed, but it should contain
        # the name of the format
        assert msg.args[0].startswith('bad char in struct format')
        assert 'abc' in msg.args[0]

    # SF bug #1512582 -- struct.error doesn't say what the repeat count is
    try:
        _struct.Struct('0' * 50000)
    except _struct.error as msg:
        assert msg.args[0].startswith('repeat count')
        assert '50000' in msg.args[0]

    # SF bug #1512582 -- struct.error doesn't say what the repeat count is
    try:
        _struct.Struct('abc' * 50000)
    except _struct.error as msg:
        assert msg.args[0].startswith('bad char in struct format')
