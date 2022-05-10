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

# UTF-8 is the same as UCS-4 and can encode all Unicode characters
encoding_list = ["utf_8", "utf_16", "utf_16_be", "utf_16_le", "utf_32", "utf_32_be", "utf_32_le"]
encoding = random.choice(encoding_list)

# If encoding is UTF-8, reencodings are noops.
# (The code below assumes all reencodings are noops, so we need to force that.)
if encoding == 'utf_8':
    encoding_list = ['utf_8']

# When we are decoding, we replace \x00 with a one-byte character
replacement_list = ["add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]
replacement = random.choice(replacement_list)

# In some cases, we will decode a single byte.
# In other cases, we will decode a multi-byte sequence.
# If we have multiple reencodings, we might even have a mix of reencod
