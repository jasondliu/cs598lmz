import codecs
# Test codecs.register_error()

import codecs

def force_unicode(s, errors='strict'):
    """
    Force a bytestring to become a Unicode string.
    """
    if isinstance(s, unicode):
        return s
    else:
        return s.decode('utf-8', errors)

class UnicodeDammit(object):
    """
    Turns a HTML page encoded in some encoding into a Unicode string.

    If the encoding is detected, returns a tuple (unicode string,
    original encoding).

    If no encoding is detected, returns (None, None).
    """
    def __init__(self, markup, overrideEncodings=None, smartQuotesTo=None,
                 isHTML=False):
        self.declaredHTMLEncoding = None
        self.markup, self.declaredHTMLEncoding = self._detectEncoding(
            markup, isHTML=isHTML)
        if self.markup is None:
            self.originalEncoding = None
            return
        self.smartQuotesTo = smartQuotesTo
        self.t
