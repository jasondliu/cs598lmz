import codecs
codecs.register_error('surrogate_or_unparsable', codecs.surrogateescape)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.NEWLINES = re.compile(r'\s+')
        self.dataArray = []
        self.tagRead = 0
        self.dataRead = 0
        self.tags = {'a':'','abbr':'','address':'','area':
        '','article':'','aside':'','audio':'','b':'','base':'','bdi':'','bdo':
        '','blockquote':'','body':'','br':'','button':'','canvas':'','caption':'',
        'cite':'','code':'','col':'','colgroup':'','data':'','datalist':'',
        'dd':'','del':'','details':'','dfn':'','dialog':'','div':'','dl':'',
        'dt':'
