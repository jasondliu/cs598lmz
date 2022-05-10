import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_main():
    for encoding, errors in [("utf-8", "add_one_codepoint"),
                             ("utf-16", "add_utf16_bytes"),
                             ("utf-32", "add_utf32_bytes")]:
        for input in ["abc", "abc\ud800", "\ud800abc", "abc\udfff",
                      "abc\ud800\udfff"]:
            for decoder_errors in ["strict", errors]:
                for encoder_errors in ["strict", errors]:
                    try:
                        decoded = input.encode(encoding, encoder_errors).\
                                      decode(encoding, decoder_errors)
                    except UnicodeEncodeError:
                        decoded = None
                    except UnicodeDecodeError:
                        decoded = None
                    if decoded != input:
                        print("Failed for", repr(input), "with",
                              "encoding=%r" % encoding,
                              "decoder_errors=%r" % decoder_errors,
                              "encoder_errors=%
