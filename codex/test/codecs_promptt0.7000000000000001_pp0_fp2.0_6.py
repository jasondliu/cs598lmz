import codecs
# Test codecs.register_error()
# Assumes that 'ascii' encoding is available for testing purposes
import encodings.ascii

def to_unicode_be(error):
    return u"%s\N{euro sign}BE"%error.object[error.start:error.end], error.end
def to_unicode_le(error):
    return u"%s\N{euro sign}LE"%error.object[error.start:error.end], error.end

# Tests on 'replace' and 'ignore'
