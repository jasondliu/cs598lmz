import codecs
# Test codecs.register_error
def ignore_me(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
codecs.register_error('ignore', ignore_me)
u = u'abc\u20acdef'
u.encode('ascii', 'ignore')
u.encode('ascii', 'strict')
# Write a file with utf-8 content
f = open('test.txt', 'w')
f.write(u.encode('utf-8'))
f.close()
# Read the file back with the codec error handler
f = open('test.txt')
codecs.getreader('utf-8')(f, 'ignore')
# Test codecs.register_error('backslashreplace')
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
u = u'abc\u20acdef'
u.encode('ascii', 'backslashreplace')
# Test codecs.lookup
codecs.lookup('utf-
