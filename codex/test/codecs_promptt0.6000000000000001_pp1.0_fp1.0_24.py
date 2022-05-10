import codecs
# Test codecs.register_error
import codecs
def bad_decode_handler(ex):
    return (u'/xFF', ex.end)
codecs.register_error('bad-decode', bad_decode_handler)
codecs.register_error('bad-decode', bad_decode_handler)
