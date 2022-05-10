import codecs
# Test codecs.register_error, bug #1135894
codecs.register_error('test.lookup', lambda x: (u'', x.start + 1))
codecs.register_error('test.strict', lambda x: (u'', x.start + 1))
codecs.register_error('test.replace', lambda x: (u'', x.start + 1))
codecs.register_error('test.ignore', lambda x: (u'', x.start + 1))

def test(encoding):
    # bug #1135894
    u = u'\u3042\u0fff'
    for errors in ('strict', 'replace', 'ignore'):
        for final in (None, False, True):
            print errors, final, encoding
            s = u.encode(encoding, errors)
            u1 = s.decode(encoding, errors)
            u2 = s.decode(encoding, 'test.' + errors)
            if final is not None:
                s = s.decode(encoding, errors, final)
               
