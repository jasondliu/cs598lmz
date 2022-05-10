import codecs
# Test codecs.register_error()

# The test is a bit lame, but it is better than nothing.

import codecs
import encodings

def test():
    def raise_error(exc):
        raise exc

    def ignore_error(exc):
        return (u"", exc.end)

    def replace_error(exc):
        return (u"?", exc.end)

    def xmlcharrefreplace_error(exc):
        return (u"&#%d;" % ord(exc.object[exc.start]), exc.end)

    def backslashreplace_error(exc):
        return (u"\\x%02x" % ord(exc.object[exc.start]), exc.end)

    def namereplace_error(exc):
        return (u"\\N{%s}" % exc.object[exc.start], exc.end)

