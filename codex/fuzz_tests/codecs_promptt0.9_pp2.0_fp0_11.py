import codecs
# Test codecs.register_error

def handler(ex):
    pass

utf8 = codecs.lookup('utf-8')
for i in (handler, codecs.ignore_errors, codecs.replace_errors,
          codecs.xmlcharrefreplace_errors, None):
    codecs.register_error('ignore', handler)
    eq(utf8.encode('\x80', 'ignore')[0], '\ufffd')
    eq(utf8.decode(b'\x80', 'ignore')[0], u'\ufffd')
    if i:
        codecs.register_error('test', i)
        eq(utf8.encode('\x80', 'test')[0], '\ufffd')
        eq(utf8.decode(b'\x80', 'test')[0], u'\ufffd')
    else:
        try:
            codecs.register_error('test', i)
        except TypeError:
            pass
        else:
            raise TestFailed

# Issue #20170
# Test register_error applied to unicode_
