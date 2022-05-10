import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import re

# remove html markup
def strip_markup(s):
    s = re.sub(r'</?[^<>]+>', '', s)
    s = re.sub(r'\[[^\]]+\]', '', s)
    return s

# remove non-ascii characters
def strip_nonascii(s):
    return ''.join([i if ord(i)<128 else ' ' for i in s])

# remove leading and trailing whitespace
def strip_whitespace(s):
    return s.strip()

# remove everything but letters, numbers and spaces
def strip_nonalphanum(s):
    return re.sub(r'[^A-Za-z0-9 ]', '', s)

# remove everything but letters, numbers, spaces, and punctuation
def strip_nonalphanumpunct(s):
    return re.sub(r'[^A-Za-z0-9 \.,\?!;:
