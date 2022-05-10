import codecs
# Test codecs.register_error('strict',), the 'strict' codec
# was registered when this file was imported
codecs.getdecoder('strict')

# The ISO-8859-1 encoding, is where things start getting
# interesting (and unicode too)
def iso88591_decode(input, errors='strict'):
    if input=="": return (u"", 0)
    return (unicode(input[0], "iso-8859-1"), 1)
def iso88591_encode(input, errors='strict'):
    if input==u"":
        return ("", 0)
    try:
        return (input[0].encode("iso-8859-1"), 1)
    except UnicodeEncodeError:
        # Python will automatically try this again with "ignore"
        # or "xmlcharrefreplace". So, we can just return an error
        # for now
        raise UnicodeEncodeError, ("iso-8859-1", input, 0, 1, "")

# Register the ISO-8859-1 codec
codecs.register(iso88
