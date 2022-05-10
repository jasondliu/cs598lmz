import codecs
# Test codecs.register_error('test', codecs.replace_errors)
a = b'\xc2\xc3'
codecs.register_error('test', codecs.replace_errors)
a.decode('utf-8', 'test')
codecs.register_error('strict', codecs.strict_errors)
a.decode('utf-8', 'strict')
codecs.register_error('ignore', codecs.ignore_errors)
a.decode('utf-8', 'ignore')
codecs.register_error('test', codecs.xmlcharrefreplace)
a.decode('utf-8', 'test')

# Issue #7953
codecs.register_error('test', lambda exc: (u'', exc.end))
a.decode('utf-8', 'test')

# Issue #7954
codecs.register_error('test', lambda exc: (u'\x00', exc.end))
a.decode('utf-8', 'test')

# Issue #7955
codecs.register_error('test',
