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

# This is a test for bug #12881, which only kicks in on
# UCS4 builds.
import sys
if sys.maxunicode > 65535:
    b'\x80\xff'.decode("utf-32be", "add_utf32_bytes")

if sys.maxunicode == 65535:
    b'\x80\xff'.decode("utf-16be", "add_utf16_bytes")
    b'\x80\xff'.decode("utf-16le", "add_utf16_bytes")

# Run the tests from bug #12881
try:
    b'\x80\xff'.decode("utf-16be", "add_one_codepoint")
except UnicodeDecodeError as exc:
    print(exc.args)
    print(exc.object)
    print(exc.start)
    print(exc.end)
    print(exc.reason)
    print(repr(exc.object[exc.start:exc.end]))

try:
    b'\x80\xff'.dec
