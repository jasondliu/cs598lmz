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

from test import support, test_unicode
from test.test_utf8 import UTF8BytesEscapeCodecTest
from test.test_unicode import UnicodeInternalEscapeCodecTest
import unittest

# TODO: Understand why _codecs_cn doesn't have a 'utf-16' tests
for encoding in [
    "cp037",
    "iso8859-1", "iso8859-15",
    "iso2022_jp", "iso2022_jp_2", "iso2022_jp_2004",
    "iso2022_kr", "iso2022_kr_2",
    "johab",
    "shift_jis", "shift_jisx0213", "shift_jis_2004",
    "cp949",
    "cp950",
    "cp1006",
    "cp1026",
    "cp1125",
    "cp1140",
    "cp874",
    "cp875",
    "cp932",
    "cp855",
    "cp856",
    "cp
