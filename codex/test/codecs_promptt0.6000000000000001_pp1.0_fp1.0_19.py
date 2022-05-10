import codecs
# Test codecs.register_error
def ignore_me(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
codecs.register_error('ignore', ignore_me)
u = u'abc\u20acdef'
u.encode('ascii', 'ignore')
