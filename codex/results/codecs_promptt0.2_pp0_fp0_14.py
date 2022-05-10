import codecs
# Test codecs.register_error()

import codecs

def test(name, enc):
    print '-'*50
    print 'Encoding:', enc
    print 'Codec:', name
    print '-'*50
    text = u'pi: \u03c0'
    print 'Original:', text
    print 'Encoded :',
    try:
        enc_text = text.encode(enc)
    except UnicodeError, err:
        print 'ERROR:', err
    else:
        print enc_text
        print 'Decoded :', enc_text.decode(enc)

def search_function(encoding):
    if encoding != 'test':
        return None
    class Codec(codecs.Codec):
        def encode(self, input, errors='strict'):
            return codecs.charmap_encode(input, errors,
                                         {ord(u'\u03c0'): u'\ufffd'})
        def decode(self, input, errors='strict'):
            return codecs.charmap_decode(input,
