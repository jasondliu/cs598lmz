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

def get_too_many_codepoints(codec_name,
                            test_str,
                            h_str,
                            h_str_bytes,
                            toowide_str,
                            toowide_str_bytes,
                            use_encode_error,
                            use_decode_error):
    for encoding in "utf-8", "utf-16", "utf-32":
        if not codec_name in codecs.encode.encodings:
            if codec_name == "mbcs":
                continue
            raise CodecLookupError("%s codec is not found"%codec_name)
        encoding_encoder = codecs.getencoder(encoding)
        encoding_decoder = codecs.getdecoder(encoding)
        test_str_bytes = encoding_encoder(test_str)[0]
        if use_encode_error == "ignore":
            test_str_bytes_ignore = test_str_bytes
        elif use_encode_error == "replace":
            test_str
