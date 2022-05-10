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

def main():
    # UTF-7: +ADw- represents a Unicode codepoint U+0061 (LATIN SMALL LETTER A)
    f = codecs.getincrementaldecoder("utf-7")()
    out, consumed, errored = f.decode(b"+ADw", final=True)
    if consumed != 4:
        print('FAILED: +ADw- does not decode completely')
    if out != "\ud800":
        print('FAILED: +ADw- does not decode to U+D800')
    f = codecs.getincrementaldecoder("utf-7")()
    out, consumed, errored = f.decode(b"+ADw+ADw", final=True)
    if consumed != 8:
        print('FAILED: +ADw+ADw- does not decode completely')
    if out != "\ud800\ud800":
        print('FAILED: +ADw+ADw- does not decode to U+D800 U+D800')
    f = codecs.getincre
