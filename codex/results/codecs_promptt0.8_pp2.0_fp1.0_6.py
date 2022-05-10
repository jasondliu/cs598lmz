import codecs
# Test codecs.register_error
codecs.register_error('ierror', codecs.ignore_errors)
codecs.register_error('strerror', codecs.strict_errors)
codecs.register_error('replace', codecs.replace_errors)
codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
codecs.register_error('namereplace', codecs.namereplace_errors)
# Test codecs.lookup_error
codecs.lookup_error('ierror')
codecs.lookup_error('strerror')
codecs.lookup_error('replace')
codecs.lookup_error('xmlcharrefreplace')
codecs.lookup_error('backslashreplace')
codecs.lookup_error('namereplace')

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_
