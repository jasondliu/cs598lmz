import codecs
# Test codecs.register_error

def f_handler(exception):
    print '%r in %s' % (exception, exception.object[exception.start:exception.end])

codecs.register_error('my.code', f_handler)

e = '%s\x01%s' % (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)
codecs.decode(e, 'utf-16')

codecs.decode(e, 'my.code')
