import codecs
# Test codecs.register_error

# Register an error handler
def bad_func(error):
    raise error

codecs.register_error('bad_func', bad_func)

# Register another error handler
def bad_func2(error):
    raise error

codecs.register_error('bad_func2', bad_func2)

# Test the error handlers
def test(encoding, errors, input, expected):
    assert codecs.encode(input, encoding, errors) == expected

def test_error(encoding, errors, input, expected):
    try:
        codecs.encode(input, encoding, errors)
    except UnicodeEncodeError as e:
        assert e.encoding == encoding
        assert e.reason == input
        assert e.object == input
        assert e.start == 0
        assert e.end == len(input)
        assert e.startswith('bad_func')
    else:
        assert 0, 'expected exception'

