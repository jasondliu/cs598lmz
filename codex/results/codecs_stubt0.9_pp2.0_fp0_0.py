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

def decoder_buffer_overflow(encoding, name, len_encoded_text,
                            len_additional_bytes):
    """
    The problem:
    If a codec replaces a character in the input stream, the decoder uses
    the same number of bytes.  For example, in UTF-16, u'\u0800' is
    represented with 2 bytes.  If you replace that by "a", the decoder
    consumes only one byte, shifts that into the current character, and
    looks for another byte.  Since there is none, a Buffer Overflow is
    raised.

    The solution:
    Add a few spaces to the data so the decoder can consume the required
    amount of bytes and keeps on decoding:
    u'\u0800'.encode('utf-16') + b'ab'

    """
    utf_16 = ['utf-16', 'utf-16-be', 'utf-16-le']
    utf_32 = ['utf-32', 'utf-32-be', 'utf-32-le']
    latin_1 = ['
