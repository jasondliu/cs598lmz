import codecs
# Test codecs.register_error()

# Create a dummy codec.
coding_spec = "testcodec"
encode = lambda input, errors: (input, len(input))
decode = lambda input, errors: (input, len(input))
register = lambda name: codecs.CodecInfo(
    name=name,
    encode=encode,
    decode=decode,
    incrementalencoder=None,
    incrementaldecoder=None,
    streamreader=None,
    streamwriter=None,
)

codecs.register(lambda name: codecs.lookup(coding_spec) if name == "testcodec" else None)

# Register an error handler which doesn't exist.
