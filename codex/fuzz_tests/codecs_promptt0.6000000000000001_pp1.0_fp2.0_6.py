import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.errorhandler', handler)

assert codecs.lookup_error('test.errorhandler') == handler

# The following unicode string contains two characters which are
# undefined in latin-1.
s = u'\u00c5\u00c6'

# Encode it with error handler "test.errorhandler", which just
# skips the characters.
assert codecs.encode(s, 'latin-1', 'test.errorhandler') == b''

# The following unicode string contains an undefined character.
s = u'\u00c5'

# Encode it with error handler "test.errorhandler", which just
# skips the character.
assert codecs.encode(s, 'latin-1', 'test.errorhandler') == b''

# The following unicode string contains two characters which are
# undefined in latin-1.
s = u'\u00c5\u00c6'

#
