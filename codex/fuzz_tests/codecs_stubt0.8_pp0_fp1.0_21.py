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

print('abc'.encode('shift_jis', 'add_one_codepoint'))
print('abc'.encode('utf-16', 'add_utf16_bytes'))
print('abc'.encode('utf-32', 'add_utf32_bytes'))
print(b'abc\x80'.decode('shift_jis', 'add_one_codepoint'))
print(b'\xff\xfea\x00bc\x00'.decode('utf-16', 'add_utf16_bytes'))
print(b'\xff\xfe\x00\x00a\x00\x00\x00bc\x00\x00\x00'.decode('utf-32', 'add_utf32_bytes'))

# This tests the backport of bpo-21551
import sys
import os
import re
import subprocess

sys.path.append("scripts")
import pyspecific

if sys.implementation.name == 'pypy':
    pypy_interpreter = sys.executable

