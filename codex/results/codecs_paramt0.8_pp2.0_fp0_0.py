import codecs
codecs.register_error("ignore_truncate", codecs.lookup_error("ignore"))

def unicode_fix(s, charset='utf-8', errors='strict'):
    if isinstance(s, unicode):
        return s
    else:
        return unicode(s, charset, errors=errors)

def utf8_fix(s, charset='utf-8', errors='strict'):
    return unicode_fix(s, charset=charset, errors=errors).encode('utf-8')

unicode_fix_latin1 = partial(unicode_fix, charset='latin-1')
unicode_fix_latin1_ignore = partial(unicode_fix, charset='latin-1', errors='ignore_truncate')

utf8_fix_latin1 = partial(utf8_fix, charset='latin-1')
utf8_fix_latin1_ignore = partial(utf8_fix, charset='latin-1', errors='ignore_truncate')


class FreenetPacket
