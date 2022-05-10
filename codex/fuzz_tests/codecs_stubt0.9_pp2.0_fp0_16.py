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

utf_7 = codecs.getencoder('utf-7')
utf_7_dec = codecs.getdecoder('utf-7')
utf_16 = codecs.getencoder('utf-16')
utf_16_dec = codecs.getdecoder('utf-16')
utf_32 = codecs.getencoder('utf-32')
utf_32_dec = codecs.getdecoder('utf-32')

inputs = ['André the Giant', '鯰篕', '𩸽母']

# UTF-7 does not round-trip on purpose
# decode input with 'replace' to get closest match in UTF-16
utf_16_out = [item.encode('utf-16', errors='replace').decode('utf-16-be') for item in inputs]
utf_32_out = [item.encode('utf-32', errors='replace').decode('utf-32-be') for item in inputs]

# Reduces the false positive rate, but not the false negative rate
def verify_blind(enc_func
