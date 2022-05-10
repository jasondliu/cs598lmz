import codecs
# Test codecs.register_error('my_strict', my_strict)
# UnicodeDecodeError: 'my_strict' codec can't decode byte 0xff in position 0: illegal multibyte sequence
# codecs.register_error('my_strict', my_strict)
# codecs.register_error('my_replace', my_replace)

def my_replace(exception):
    print(exception)
    return ('', exception.start + 1)

codecs.register_error('my_replace', my_replace)
data = b'abc\xff\xfe\x00\x01'
