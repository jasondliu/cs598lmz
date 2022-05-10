import codecs
# Test codecs.register_error() and codecs.lookup_error()
for name in ('strict', 'ignore', 'replace', 'xmlcharrefreplace',
             'backslashreplace', 'namereplace'):
    try:
        codecs.lookup_error(name)
    except LookupError:
        print('Failed to lookup error handler %s' % name)

# Test codecs.register_error() and codecs.lookup_error()
def bad_handler(exc):
    print('Handling exception:', exc)
    raise TypeError
codecs.register_error('test.bad_handler', bad_handler)

try:
    codecs.lookup_error('test.bad_handler')
except LookupError:
    print('Failed to lookup error handler test.bad_handler')

try:
    codecs.lookup_error('bad.handler')
except LookupError:
    print('Failed to lookup error handler bad.handler')

codecs.register_error('test.test_bad_handler', bad_handler)

try:
    codecs
