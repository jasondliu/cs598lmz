import codecs
# Test codecs.register_error

def handler(ex):
    pass

utf8 = codecs.lookup('utf-8')
for i in (handler, codecs.ignore_errors, codecs.replace_errors,
          codecs.xmlcharrefreplace_errors, None):
    codecs.register_error('ignore', handler)
