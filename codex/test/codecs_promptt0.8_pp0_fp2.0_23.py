import codecs
# Test codecs.register_error('replace_with_space', replace_with_space)
# def transform(s):
#     return s.translate(None, '"|&')

def transform(s):
    s = re.sub(r'&#(\d+);', r'#\1', s)
    s = re.sub(r'&amp;', '&', s)
    s = re.sub(r'&lt;', '<', s)
    s = re.sub(r'&gt;', '>', s)
    s = re.sub(r'&quot;', '"', s)
    s = re.sub(r'&#(\d+);', r'#\1', s)
    s = re.sub(r'(' + '|'.join(_puctuation_chars) + ')', r' \1 ', s)
    s = re.sub(r'#(\d+)', r'&#\1;', s)
    s = s.replace('*', '')
    return s

