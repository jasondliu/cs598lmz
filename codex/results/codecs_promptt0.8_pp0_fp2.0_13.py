import codecs
# Test codecs.register_error
def handle_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        text = u'ASCII encoding error: '
    elif isinstance(exc, UnicodeDecodeError):
        text = u'ASCII decoding error: '
    else:
        raise TypeError("don't know how to handle %r" % exc)
    print '===>', text + str(exc)
    return (u'\ufffd', str(exc)[0])  # return the replacement character
codecs.register_error('test.ascii', handle_error)
print '===>', 'abcd'.decode('ascii', 'test.ascii')

# Test setlocale
# Note: These tests are incomplete.
import locale
# See if the current locale doesn't use the right values.
locale.setlocale(locale.LC_ALL, '')
s = '%.2d' % 2
if s != '02': print '===>', s
locale.setlocale(locale.LC_ALL, 'C')
s = '%.
