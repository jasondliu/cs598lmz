import codecs
codecs.register_error('strict', codecs.lookup('utf8'))
codecs.register_error('replace', codecs.lookup('replace'))
codecs.register_error('ignore', codecs.lookup('ignore'))

class NParser(HTMLParser, object):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = None

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'ul':
            self.data = []
        elif tag == 'li':
            self.item = {}
        elif tag == 'a' and self.item != None:
            self.item['name'] = _attr(attrs, 'title')
            self.item['url'] = _attr(attrs, 'href')

    def handle_endtag(self, tag):
        if tag == '
