import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

def _unescape(s):
    # Replace any &xx; or &#xxx; with the corresponding character
    s = re.sub(r'&#(\d\d\d);', lambda m: chr(int(m.group(1))), s)
    s = re.sub(r'&#x([0-9a-fA-F]{2});', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'&(\w+);', lambda m: unescape(m.group(1)), s)
    return s

def _unescape_attr(s):
    # Replace any &xx; or &#xxx; with the corresponding character
    s = re.sub(r'&#(\d\d\d);', lambda m: chr(int(m.group(1))), s)
