import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

LIMIT = 10000
S_RES = 'result'
S_ID = 'id'
S_CLASS = 'class'
S_NAME = 'name'
IGNORE_TAGS = set([u'w:tbl', u'w:tc', u'v:wordart', u'w:tblPr', u'w:tblGrid', u'w:tcPr', u'w:pPr', u'w:rPr'])

class Word2TexError(Exception):
    def __init__(self, msg):
        # Call the base class constructor with the parameters it needs
        super(WordError, self).__init__(msg)


class AnnoyingAPI(object):
    @classmethod
    def unescape(cls, s):
        p = htmllib.HTMLParser(None)
        p.save_bgn()
        p.feed(s)
        return p.save_end()


def ns_format(tag, cls, id):
    s = ''
