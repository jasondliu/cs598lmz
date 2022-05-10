import codecs
# Test codecs.register_error
# Author: Steffen Daode Nurpmeso <steffen@sdaoden.eu>

import codecs

def test_main():
    def custom_ignore_error(exc):
        return (u"@", 1)
    def custom_replace_error(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (u"@", 1)
        elif isinstance(exc, UnicodeDecodeError):
            return (u"A", 1)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    def custom_xmlcharrefreplace_error(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (u"@", 1)
        elif isinstance(exc, UnicodeDecodeError):
            return (u"&#65;", 1)
        else:
            raise TypeError("don't know how to handle %r" % exc)
