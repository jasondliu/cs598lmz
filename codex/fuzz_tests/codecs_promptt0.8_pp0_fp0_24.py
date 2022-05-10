import codecs
# Test codecs.register_error

# Decoding is supported but should behave as if they didn't exist
for cls in (codecs.LookupError, LookupError, ValueError):
    # Bug#1672300: NotImplementedError raised for non-existent error handlers.
    codecs.register_error('test', lambda x: (u'', 0))
    codecs.lookup_error('test')
    codecs.lookup_error('ignore')
    codecs.lookup_error('replace')
    codecs.lookup_error('xmlcharrefreplace')
    codecs.lookup_error('backslashreplace')
    codecs.lookup_error('surrogateescape')
    codecs.lookup_error('surrogatepass')
    codecs.lookup_error('strict')

    # Bug#1672300: NotImplementedError raised for non-existent error handlers.
    codecs.register_error('test', lambda x: (u'', 0))
    codecs.lookup_error('test')
    codecs.lookup_error('ignore')

