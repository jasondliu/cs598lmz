import codecs
codecs.register_error('strict', codecs.ignore_errors)

def clean(s):
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('&amp;', '&')
    s = s.replace('&lt;', '<')
    s = s.replace('&gt;', '>')
    s = s.replace('&apos;', '\'')
    s = s.replace('&quot;', '"')
    s = s.replace('&#xA;', ' ')
    s = s.replace('&#xD;', ' ')
    s = s.replace('\x00', ' ')
    return s

def extract_text(filename):
    try:
        with open(filename, 'rb') as f:
            xml = f.read()
    except:
        return '', ''
    try:
        tree = ET.fromstring(xml)
    except:
        return '', ''
    try:
        title = tree.
