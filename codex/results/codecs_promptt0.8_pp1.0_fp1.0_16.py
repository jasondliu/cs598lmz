import codecs
# Test codecs.register_error('decoder_error', my_decoder)

def my_decoder(ex):
    print('my_decoder called with:', ex)
    return (u'',ex.start + 1)

codecs.register_error('decoder_error', my_decoder)

s = 'ℵ'
s_utf8_bytes = s.encode('utf-8')
print(s_utf8_bytes)
# buffer = codecs.getreader('utf-8')(io.BytesIO(s_utf8_bytes))
#buffer = io.BytesIO(s_utf8_bytes)
buffer = s.encode('utf-8')

# NOTE: When the error_handler argument is used, the source string is encoded before the error handler is called.
# When an error handler is not used, the source string is decoded after the conversion is completed.
# s_utf8_decoded = io.TextIOWrapper(buffer, encoding='utf-8', errors='decoder_error')
s_utf8_decoded = io.TextIOWra
