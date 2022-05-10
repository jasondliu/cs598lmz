import codecs
# Test codecs.register_error() and its codecs (encodings).
# This also tests codecs.replace_errors().

# No UnicodeEncodeError because of patent issues
# Codecs which generate UnicodeDecodeErrors
badencodings = ["ascii", "base64_codec", "quopri_codec"]

def test_bad_encoding_big5(badenc):
    with codecs.open('non-existent', encoding=badenc, errors='strict') as f:
        pass
    try:
        s = badencodings.decode(badenc)
    except (LookupError, AttributeError):
        # Some codecs are available only as encodings
        return
    with codecs.open('non-existent', encoding=badenc, errors='strict') as f:
        pass

def test_bad_encoding_latin1(badenc):
    with codecs.open('non-existent', encoding=badenc, errors='strict') as f:
        pass
