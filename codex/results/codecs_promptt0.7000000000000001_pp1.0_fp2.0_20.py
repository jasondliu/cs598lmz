import codecs
# Test codecs.register_error('decode_noop', decode_noop)
codecs.getincrementaldecoder('utf8')().decode_noop("abc")

# Test codecs.lookup_error('decode_noop')
codecs.lookup_error("decode_noop")("abc")
