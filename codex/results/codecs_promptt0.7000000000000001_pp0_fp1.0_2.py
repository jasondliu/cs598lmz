import codecs
# Test codecs.register_error
def test_register_error():
    """Test the register_error() function."""
    def raise_error(exc):
        raise exc
    def ignore_error(exc):
        return (u"", exc.start + 1)
    def replace_error(exc):
        return (u"�", exc.start + 1)
    def xmlcharrefreplace_error(exc):
        # A real XML char ref would be nice, but how to know the
        # encoding here?
        return (u"&#xfffd;", exc.start + 1)
    def backslashreplace_error(exc):
        return (u"\\\\", exc.start + 1)
    def namereplace_error(exc):
        return (u"\\N{REPLACEMENT CHARACTER}", exc.start + 1)

    codecs.register_error("test.raise", raise_error)
    codecs.register_error("test.ignore", ignore_error)
    codecs.register_error("test.replace", replace_error)
    codecs.register_error("test.xmlchar
