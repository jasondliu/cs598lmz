import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_unicode(value, encoding='utf-8', errors='strict'):
    if isinstance(value, unicode):
        return value
    elif isinstance(value, basestring):
        return unicode(value, encoding, errors)
    else:
        return unicode(value)

def _normalize_whitespace(text):
    return ' '.join(text.split())

def _normalize_newlines(text):
    return '\n'.join(text.splitlines())

def _normalize_spaces(text):
    return ' '.join(text.split())

def _normalize_unicode(text):
    return unicodedata.normalize('NFC', text)

def _normalize_case(text):
    return text.lower()

def _normalize_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def _normalize_digits(text):
    return re.sub
