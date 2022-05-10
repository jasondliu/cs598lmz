import codecs
# Test codecs.register_error('xmlcharrefreplace', xmlcharrefreplace_errors)
# Decoder for HTML encoding with XML entities.
class xmlcharrefreplace_errors:
    def xmlcharrefreplace_decode(self, input, errors='strict'):
        """Decode characters using xmlcharrefreplace encoding

        The input is first decoded using the standard 'ascii' codec and
        characters that cannot be decoded are then replaced with an xml
        character reference of the form "&#YYYY" where YYYY is the code
        point value in decimal.

        errors may be given to set a different error handling scheme. Default
        is 'strict' meaning that encoding errors raise a ValueError.

        """
        return codecs.xmlcharrefreplace_encode(input, errors)[0]
# Encoder for HTML encoding with XML entities.
