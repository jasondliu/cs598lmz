import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a list of (regular expression, replacement) pairs for abbreviations:
abbreviations = [
    (r'\b([A-Za-z]\.)\s+([A-Za-z]\.)\s+([A-Za-z][a-z]+)', r'\1\2\3'),
    (r'\b([A-Za-z]\.)\s+([A-Za-z][a-z]+)', r'\1\2'),
    (r'\b([A-Z][sc][hl])\.', r'\1'),
]

def expand_abbreviations(text):
    for regex, replacement in abbreviations:
        text = re.sub(regex, replacement, text)
    return text

def read_data(filename):
    """Extract the first file enclosed in a zip file as a list of words"""
    with zipfile.ZipFile(filename) as f:
        data = f.read(f.namelist()
