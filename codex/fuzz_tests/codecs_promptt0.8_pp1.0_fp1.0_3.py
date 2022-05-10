import codecs
# Test codecs.register_error on a known encoding. If this works and doesn't
# segfault, the test is passed.
try:
    codecs.register_error('raise', lambda x: codecs.lookup_error('strict')(x))
    codecs.register_error('strict', lambda x: codecs.lookup_error('raise')(x))
    x = codecs.decode('\xff', 'iso8859-1', 'strict')
except UnicodeDecodeError:
    pass
