import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)

# UTF-16
# Invoke by "python -3" to trigger the locale.Error
if sys.version_info[0] == 3 and sys.platform.startswith('win'):
    def utf16_handler(ex):
        return (u'?', ex.end + 1)
    codecs.register_error('TestUTF16', utf16_handler)
    u'''\u9190'''.encode('utf_16')
    codecs.register_error('TestUTF16', None)


def crlf(text):
    return text.replace('\n', '\r\n')
if sys.platform.startswith('win'):
    def lf(text):
        return text.replace('\r\n', '\n')
    newline = '\r\n'
else:
    lf = crlf

