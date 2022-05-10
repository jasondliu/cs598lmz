import codecs
# Test codecs.register_error('ignore') for encodings that ignore errors.


def test_register_error_ignore():
    # Issue #1297: test various codecs against the 'ignore' error handler.
    for encoding in ('utf-16', 'utf-7', 'utf-8'):
        try:
            codecs.lookup(encoding)
        except LookupError:
            # Skip missing encodings
            continue
        for input, expected in (
            ('abc\xff', 'abc'),
            ('abc\xff\n', 'abc\n'),
            ('abc\n\xff', 'abc\n'),
            ('\xff', ''),
            ('\xff\n', '\n'),
            ('\n\xff', '\n'),
            ('\xff' * 10, ''),
            ('\xff' * 10 + '\n', '\n'),
            ('\n' + '\xff' * 10, '\n'),
            ('\n' + '\xff' * 10 + '\n', '\n\n'),
        ):
            encoded = input.encode
