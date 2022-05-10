import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
import csv
import re
import os
import string
import subprocess
import sys
import tempfile
import time
import traceback

print_debug=False
print_stop_catches_summary=False

# Matches "" and '' quotes.
quote_re = re.compile('"([^"]*?)"|\'([^\']*?)\'', re.DOTALL | re.MULTILINE | re.IGNORECASE)
whitespace_re = re.compile('\s+')

invalid_chars_re = re.compile(r'[\x01-\x1F]', re.IGNORECASE)

# Warning: The module name is used to create the output folder, so do not change it!
mod = 'Awesomenauts'

# List of language codes (ISO 639-1 alpha-2) and their corresponding languages
languages = [
    ('en', 'English'),
    ('es', '
