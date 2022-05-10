import codecs
# Test codecs.register_error()

def search_function(encoding):
    """Look for a register_error()-generated error handler for 'encoding'.

    Look for a function in the module's globals whose name is
    'codec_error_' + encoding.  If found, return it, else return None.
    """
    if encoding == 'test':
        return codecs.lookup_error('test')
    else:
        return None

codecs.register_error(search_function)
codecs.lookup_error('test')

for name in ('test', 'spam'):
    try:
        codecs.lookup_error(name)
    except LookupError as err:
        print(err, '<-- expected')
    else:
        print(name, '<-- unexpected')
