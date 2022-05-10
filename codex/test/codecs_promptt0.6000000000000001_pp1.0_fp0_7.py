import codecs
# Test codecs.register_error, bug #1135894
codecs.register_error('test.lookup', lambda x: (u'', x.start + 1))
codecs.register_error('test.strict', lambda x: (u'', x.start + 1))
codecs.register_error('test.replace', lambda x: (u'', x.start + 1))
codecs.register_error('test.ignore', lambda x: (u'', x.start + 1))

def test(encoding):
    # bug #1135894
    u = u'\u3042\u0fff'
