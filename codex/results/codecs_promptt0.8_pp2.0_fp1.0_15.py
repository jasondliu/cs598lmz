import codecs
# Test codecs.register_error()

def test_main():

    # This test currently fails if you have set the LC_CTYPE to UTF-8.
    # In that case, the encoder uses the first 2 bytes for the unicode
    # character, and the decoder doesn't notice the error (it's reset after
    # the first character, and the codepoint doesn't exist).
    if sys.platform == 'darwin':
        print 'Unicode locale not supported on Darwin, skipping test'
        return

    import codecs, encodings.latin_1

    def g(s, m=None, stop=False):
        return encodings.latin_1.encode(s, m, stop)

    codecs.register_error('g', g)

    s = u"\u20ac\u00ae"

    for errors in ('ignore','replace','xmlcharrefreplace','g','g,ignore','g,replace','g,xmlcharrefreplace'):
        # Before any calling of encode, the error handler should have
        # the default value.
        default_handler = codecs.
