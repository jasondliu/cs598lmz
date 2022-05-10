import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

class WordsByURLsTransformator(WrappedBolao):

    def __init__(self, bolao):
        WrappedBolao.__init__(self, bolao)

    def _preprocess(self):
        WrappedBolao._preprocess(self)
        self.words_by_urls = self.words_by_urls()

    def words_by_urls(self):
        words_by_urls = defaultdict(list)
        for url, words in self.words().iteritems():
            for word, count in words.iteritems():
                words_by_urls[url].append(\
                        {"word": word, "count": count})
        return words_by_urls

    def rss_items(self):
        for url in sorted(self.words_by_urls.keys()):
            yield self.to_rss_item(url)

    def to_rss_item(self, url):
        item = {}
        words = u""
       
