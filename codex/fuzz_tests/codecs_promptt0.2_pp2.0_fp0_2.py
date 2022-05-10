import codecs
# Test codecs.register_error
def search_function(encoding):
    print('search_function({})'.format(encoding))
    if encoding == 'test.unicode':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Test codecs.lookup_error
def replace_function(exc):
    print('replace_function({})'.format(exc))
    if isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    return (u'?', exc.end)

codecs.register_error('test.replace', replace_function)

# Test codecs.lookup_error
def ignore_function(exc):
    print('ignore_function({})'.format(exc))
    if isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    return (u'?', exc.end)

codecs.register_error('test.ignore', ignore_function)

# Test codecs.lookup_error
def xmlcharref
