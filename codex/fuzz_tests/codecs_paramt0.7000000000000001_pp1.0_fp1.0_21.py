import codecs
codecs.register_error('strict', codecs.ignore_errors)
table = { ord(u'\u2018') : u"'",
          ord(u'\u2019') : u"'",
          ord(u'\u201c') : u'"',
          ord(u'\u201d') : u'"',
          ord(u'\u2013') : u'-',
          ord(u'\u2014') : u'-',
          ord(u'\u2022') : u'*',
          ord(u'\u2026') : u'...',
          ord(u'\u00b6') : u'*'
          }

def clean(s):
    """
    Strips the string and converts it to unicode
    """
    return unicode(s.strip(), 'utf-8').translate(table).encode('utf-8')


def convert(filename):
    """
    Converts the given document to a dict
    """
    result = []
    f = codecs.open(filename, encoding='utf-8', errors='strict')
    for
