import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 76. How to format a specified string to limit the number of characters to 6?

# Sample string: 'The quick brown fox jumps over the lazy dog.'

import textwrap
s = 'The quick brown fox jumps over the lazy dog.'
res = textwrap.shorten(s, width=24, placeholder="...")
print(res)

# 77. How to check if a given string is a valid URL?

# Input
# 'https://www.python.org/'

import re
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
match = pattern.match('https://www.programiz.com/')

print(bool(match))

# 78. How to find all adverbs and their positions in a given sentence?

# Input
# "Clearly, he has no excuse for such behavior."

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

sen = "Clearly, he
