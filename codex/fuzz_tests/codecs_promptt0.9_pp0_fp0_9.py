import codecs
# Test codecs.register_error, ensure that errors prior to register can be
# re-raised.

def name(encoding):
    if encoding == 'rot13':
        return 'test'
    return None

codecs.register_error('test', name)

assert codecs.strict_errors == codecs.strict_errors  # crash
assert codecs.replace_errors == codecs.replace_errors  # ignore
assert codecs.ignore_errors == codecs.ignore_errors  # replace

try:
    b"hello".decode('rot13')
    assert False
except UnicodeError:
    pass

# Test codecs.lookup_error, ensure that errors prior to register can be
# re-raised.

assert codecs.strict_errors(None, 'rot13') == 'strict'  # crash
assert codecs.replace_errors(None, 'rot13') == 'replace'  # ignore
assert codecs.ignore_errors(None, 'rot13') == 'ignore'  # replace

try:
    b"hello".decode('rot13')
    assert
