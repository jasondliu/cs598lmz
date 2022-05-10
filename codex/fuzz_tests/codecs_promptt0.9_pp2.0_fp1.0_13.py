import codecs
# Test codecs.register_error("ignore", encoding_error_handler)
# Not used (error is catched by translate())

def to_unicode(s, encoding='utf-8'):
    """
    Convert a string to unicode.
    """
    if len(s) == 0:
        return u''
    if isinstance(s, unicode):
        return s
    try:
        decoded = s.decode(encoding)
    except UnicodeDecodeError:
        # Apache mod_wsgi logs errors from sys.stdout, which means
        # we can sometimes end up here. We have to do something with
        # these so we simply replace non-decodable characters with
        # '?' to allow logging to continue.
        decoded = s.decode(encoding, 'replace')
    return decoded
        
class StreamingBuffer(object):
    """
    An in-memory buffer that supports streaming.

    >>> buffer = StreamingBuffer()
    >>> buffer.write('foo')
    >>> buffer.read(1)
    'f'
    >>> buffer.read(1)
    '
