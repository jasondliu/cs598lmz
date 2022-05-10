import codecs
# Test codecs.register_error('test', lambda x: u'[warning]')
# and try to decode a string with a bad character
# in it (u'\ud800')
new_codec_error = codecs.register_error('test', lambda x: u'[warning]')
