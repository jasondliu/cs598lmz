import codecs
# Test codecs.register_error
# This should raise LookupError
codecs.register_error('no-such-errorhandler', None)

# This should raise ValueError
codecs.register_error('no-such-errorhandler', 42)

# This should raise LookupError
codecs.register_error('no-such-errorhandler', 'no-such-errorhandler')

# This should raise ValueError
codecs.register_error('no-such-errorhandler', lambda x,y,z:None)

# This should raise LookupError
codecs.register_error('strict', 'no-such-errorhandler')

# This should raise ValueError
codecs.register_error('strict', lambda x,y,z:None)

# This should work
codecs.register_error('strict', codecs.strict_errors)

# Check that the errorhandler we registered is used for encoding/decoding.
# This should raise an UnicodeEncodeError
u'\xff'.encode('latin-1', 'strict')

# This should raise an
