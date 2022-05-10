import codecs
# Test codecs.register_error
def codec_error_handler(exception):
    if exception.object[exception.start] == 'X':
        return (u'Y',exception.end)
    else:
        return (u'?',exception.end+1)

codecs.register_error('test.codec',codec_error_handler)

