import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    return (u'', exception.start + 1)

codecs.register_error('my_error', my_error)

utf8_reader = codecs.getreader('utf-8')

def my_utf8_reader(*args, **kwargs):
    reader = utf8_reader(*args, **kwargs)
    reader.errors = 'my_error'
    return reader

