import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

print codecs.decode('\xff', 'ascii', 'my_replace')
print codecs.decode('\xff', 'ascii', 'replace')
print codecs.decode('\xff', 'ascii', 'ignore')

print codecs.decode('\xff\xff', 'ascii', 'my_replace')
print codecs.decode('\xff\xff', 'ascii', 'replace')
print codecs.decode('\xff\xff', 'ascii', 'ignore')

print codecs.decode('\xff\xff\xff', 'ascii', 'my_replace')
print codecs.decode('\xff\xff\xff', 'ascii', '
