import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _unicode(s):
    if isinstance(s, str):
        return s.decode('utf8', 'strict')
    elif isinstance(s, unicode):
        return s
    else:
        raise TypeError('Not a string')

def _str(s):
    if isinstance(s, str):
        return s
    elif isinstance(s, unicode):
        return s.encode('utf8', 'strict')
    else:
        raise TypeError('Not a string')

def _numeric(s):
    if isinstance(s, (int, float, long)):
        return s
    try:
        return float(s)
    except ValueError:
        raise TypeError('Not a number')

def _bool(s):
    if isinstance(s, bool):
        return s
    if isinstance(s, (int, float, long)):
        return bool(s)
    if isinstance(s, (str, unicode)):
       
