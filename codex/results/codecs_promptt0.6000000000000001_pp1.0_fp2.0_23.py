import codecs
# Test codecs.register_error
import sys
if sys.version_info < (3, 0):
    import encodings.ascii
    encodings.ascii.Codec.name
    encodings.ascii.Codec.encode
    encodings.ascii.Codec.decode
    encodings.ascii.Codec.incrementaldecoder
    encodings.ascii.Codec.incrementalencoder
    if sys.version_info < (2, 6):
        import encodings.iso8859_3
        encodings.iso8859_3.Codec.name
        encodings.iso8859_3.Codec.encode
        encodings.iso8859_3.Codec.decode
        encodings.iso8859_3.Codec.incrementaldecoder
        encodings.iso8859_3.Codec.incrementalencoder
    import encodings.iso8859_15
    encodings.iso8859_15.Codec.name
    encodings.iso
