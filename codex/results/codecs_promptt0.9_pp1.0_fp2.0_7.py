import codecs
# Test codecs.register_error()
stdin_fh = sys.stdin.detach()
stdin_encoding = getattr(stdin_fh, "encoding", None)
if stdin_encoding is not None:
    try:
        codecs.lookup_error("strict")
    except LookupError:
        codecs.register_error("strict", codecs.lookup_error("ignore"))
    try:
        codecs.lookup_error("surrogatepass")
    except LookupError:
        codecs.register_error("surrogatepass", codecs.lookup_error("ignore"))
    try:
        codecs.lookup_error("surrogateescape")
    except LookupError:
        e = codecs.lookup_error("ignore")

        def surrogateescape_error(exc):
            if isinstance(exc, UnicodeEncodeError):
                try:
                    x = exc.object
                    invalid_method = x.decode
                except AttributeError:
                    pass
                else:
                    exc = UnicodeDecodeError(exc.enc
