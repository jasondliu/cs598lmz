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

