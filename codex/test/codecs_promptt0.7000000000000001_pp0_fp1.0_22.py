import codecs
# Test codecs.register_error()

# test codecs.register_error
def test_register_error():
    def my_strict_error_handler(exception):
        raise exception

    def my_ignore_error_handler(exception):
        return u"", exception.end

    def my_replace_error_handler(exception):
        return u"\ufffd", exception.end

    def my_xmlcharrefreplace_error_handler(exc):
        if isinstance(exc, UnicodeEncodeError):
            s = []
            for c in exc.object[exc.start:exc.end]:
                s.append(u"&#%d;" % ord(c))
            return (u"".join(s), exc.end)
        elif isinstance(exc, UnicodeDecodeError):
            return (u"\ufffd", exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    # Get the current exception handlers
    old_handlers = codecs.lookup_error('strict')
    # Test default error handlers

