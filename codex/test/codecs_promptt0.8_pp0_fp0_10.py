import codecs
# Test codecs.register_error, raising an error from a callback that would
# otherwise be ignored.
# codecs.register_error('my.error',
# lambda e: (u'X', e.end))
# codecs.register_error('my.error',
# lambda e: (u'Y', e.end))
# codecs.register_error('my.error',
# lambda e: (u'Z', e.end))
# s = 'a\x80b\x80c'
# u = u'a\ufffd' * 3
# for errors in ['my.error',
# 'ignore',
# 'replace',
# 'strict']:
# assert s.decode('latin-1', errors) == u
# codecs.register_error('my.error',
# lambda e: (u'', e.end))
# s = 'a\x80b\x80c'
# u = u'abc'
# for errors in ['my.error',
# 'ignore',
# 'replace',
# 'strict']:
# assert s.decode('latin-
