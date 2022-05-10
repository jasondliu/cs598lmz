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

xp = "&#x3db;&euro;"
sp = unicodedata.normalize("NFC", xp)
xp = "%s%s" % (xp, chr(0x110000))
sp = "%s%s" % (sp, chr(0x110000))

sys.stdout = sys.stderr = codecs.getwriter('utf-8')(sys.stdout.buffer)

print('ENCODINGS = ' + repr(sorted(codecs.encode.__self__)))

for enc in sorted(codecs.encode.__self__):
    print('ENCODING = ' + repr(enc))
    if enc == "iso2022_jp_2":
        continue
    try:
        expected = b'\x3d\x3db\x3f\x3f\xe2\x82\xac'
        if enc == "cp949":
            expected = b'\x3d\x3db\x81\x47\x81\x48'
        if enc == "euc
