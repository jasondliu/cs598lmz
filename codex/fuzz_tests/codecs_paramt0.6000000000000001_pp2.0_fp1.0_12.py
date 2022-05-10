import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _to_unicode(text):
    if isinstance(text, unicode):
        return text
    return unicode(text, 'utf-8', 'strict')

def _to_utf8(text):
    if isinstance(text, str):
        return text
    return text.encode('utf-8')

def _to_ascii(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

def _to_lowercase(text):
    return text.lower()

def _to_uppercase(text):
    return text.upper()

def _remove_accents(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')

def _remove_punctuation(text):
    return text.translate(string.maketrans("",""), string.punctuation)

def _remove_non_alphanumeric(text):
    return re.
