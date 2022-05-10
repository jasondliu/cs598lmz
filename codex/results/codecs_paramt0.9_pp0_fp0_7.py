import codecs
codecs.register_error('restrict', restrict_unicode.restrict_unicode)

#source: http://shallowsky.com/blog/programming/python-string-restrictions.html
#replaces all non-ascii chars with a ?
def ascii_only(m, conjunction='_'):
    if conjunction not in ' \'_-()[]{}<>/!@#$%^&|':
        raise ValueError("conjunction must be one of: ' _-()[]{}<>/!@#$%^&|'")

    s = ''
    for ch in m:
        if ord(ch) < 128:
            s += ch
        else:
            s += conjunction
    return s


def ascii_concatenated_only(concatenated_text):
    s = ''
    for m in concatenated_te
