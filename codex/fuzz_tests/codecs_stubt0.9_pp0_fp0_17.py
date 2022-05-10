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

with open('iso-8859-15.enc', 'w') as outFile:
    outFile.write('''\
# -*- encoding: iso-8859-15 -*-

def decode(input, errors='strict'):
    return tuple(ord(b) for b in input) + (0x1234,), len(input)


def encode(input, errors='strict'):
    return ''.join(chr(c) for c in input), len(input)
    ''')

with open('utf-8-import.enc', 'w') as outFile:
    outFile.write('''\
# -*- coding: utf-8 -*-

def decode(input, errors='strict'):
    return tuple(ord(b) for b in input) + (0x1234,), len(input)


def encode(input, errors='strict'):
    return ''.join(chr(c) for c in input), len(input)
    ''')

from test import support


