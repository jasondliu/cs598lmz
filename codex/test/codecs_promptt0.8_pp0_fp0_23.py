import codecs
# Test codecs.register_error
def error_handler(exception):
    return (u"", exception.end)
codecs.register_error("test.replace", error_handler)
codecs.lookup_error("test.replace")
# Test codecs.lookup_error, codecs.register_error
try:
    codecs.lookup_error("missing.error")
except LookupError as e:
    assert type(e) is LookupError
# Test codecs.open, codecs.getreader
