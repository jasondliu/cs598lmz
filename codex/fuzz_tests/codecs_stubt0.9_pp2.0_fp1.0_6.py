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

coderange_error_encodings = [
    "cp932",
    "euc-jp",
    "gb2312",
    "gbk",
    "gb18030",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_3",
    "iso2022_jp_2004",
    "iso2022_jp_ext",
    "shift_jis_2004",
    "mac_roman",
    "mac_cyrillic",
    "sjis",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_16_ex,utf16:add_one_codepoint",
    "utf_16_ex,utf16:add_utf16_bytes",
    "utf_16_ex,utf32:add_utf32_bytes",
]

coderange_error_encodings_mixed = [
    "cp932",
   
