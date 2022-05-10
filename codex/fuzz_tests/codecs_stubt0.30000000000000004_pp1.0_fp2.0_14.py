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

# Test that the codecs module can be imported
import codecs

# Test that the encodings package can be imported
import encodings

# Test that the encodings package can be imported
import encodings.aliases

# Test that the encodings package can be imported
import encodings.ascii

# Test that the encodings package can be imported
import encodings.base64_codec

# Test that the encodings package can be imported
import encodings.big5

# Test that the encodings package can be imported
import encodings.big5hkscs

# Test that the encodings package can be imported
import encodings.bz2_codec

# Test that the encodings package can be imported
import encodings.charmap

# Test that the encodings package can be imported
import encodings.cp037

# Test that the encodings package can be imported
import encodings.cp1006

# Test that the encodings package can be imported
import encodings
