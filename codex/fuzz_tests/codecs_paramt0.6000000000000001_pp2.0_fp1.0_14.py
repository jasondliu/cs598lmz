import codecs
codecs.register_error('strict', codecs.replace_errors)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

def safe_unicode(obj, encoding='utf-8'):
    """ return the unicode representation of obj """
    try:
        return unicode(obj)
    except UnicodeError:
        # obj is str
        return unicode(obj, encoding, 'strict')

if __name__ == '__main__':
    pass
