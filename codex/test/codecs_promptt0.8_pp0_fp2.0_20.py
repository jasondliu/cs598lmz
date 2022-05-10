import codecs
# Test codecs.register_error to replace bad characters with a Python 'replacement'
# character
utf8reader = codecs.getreader('utf-8')
