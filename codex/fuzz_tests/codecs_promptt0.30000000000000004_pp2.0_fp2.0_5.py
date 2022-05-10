import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

for encoding in ['latin-1', 'utf-8']:
    print '%r' % encoding
    print codecs.decode('\xff', encoding, 'my_replace')
    print codecs.decode('\xff\xff', encoding, 'my_replace')
    print codecs.decode('\xff\xff\xff', encoding, 'my_replace')
    print codecs.decode('\xff\xff\xff\xff', encoding, 'my_replace')
    print codecs.decode('\xff\xff\xff\xff\xff', encoding, 'my_replace')
    print codecs.decode('\xff\xff\xff\xff\xff\xff', encoding, 'my_replace')
    print
