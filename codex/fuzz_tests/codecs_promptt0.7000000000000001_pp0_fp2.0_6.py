import codecs
# Test codecs.register_error()
# Assumes that 'ascii' encoding is available for testing purposes
import encodings.ascii

def to_unicode_be(error):
    return u"%s\N{euro sign}BE"%error.object[error.start:error.end], error.end
def to_unicode_le(error):
    return u"%s\N{euro sign}LE"%error.object[error.start:error.end], error.end

# Tests on 'replace' and 'ignore'
for (errors, codec) in (('replace', 'ascii'),
                        ('ignore', 'ascii')):
    print errors, codec
    codecs.register_error(errors, to_unicode_be)
    assert unicode("abc\x80\xffdef", errors, codec) == \
           u"abc\u0be3\u0be4def"
    codecs.register_error(errors, None)
    assert unicode("abc\x80\xffdef", errors, codec) == \
           u"abc\ufffd\uff
