import _struct
import textwrap
import functools
import sys
import unicodedata

s = "\x01\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59"
o = 0

print(_struct.unpack('<' + 'B' * 16, s[o+1:o+17]))
o +=17
print(_struct.unpack('!BBBBBBBBBBBBBBBB', s[o+1:o+17]))
o +=17
print(_struct.unpack('<' + 'h' * 8, s[o+1:o+17]))
o +=17
print(_struct.unpack('<' + 'H' * 8, s[o+1:o+17]))
o +=17
print(_struct.unpack('<' + 'i' *
