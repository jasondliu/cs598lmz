import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a list of (regular expression, replacement) pairs for abbreviations:
abbreviations = [
    (r'\b([A-Za-z]\.)\s+([A-Za-z])', r'\1\2'),
    (r'\b(\d+)(st|nd|rd|th)\b', r'\1'),
    (r'\b(\d+)([a-zA-Z])\b', r'\1 \2'),
    (r'\b(\d+)(\s*)([a-zA-Z])\b', r'\1\3'),
    (r'\b(\d+)(\s*)([a-zA-Z])\b', r'\1\3'),
    (r'\b(\d+)(\s*)([a-zA-Z])\b', r'\1\3'),
    (r'\b(\d+)(\s*)([a-zA-Z])\b', r'\
