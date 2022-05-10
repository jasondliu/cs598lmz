import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class NaverKeywordCrawler(object):
    def __init__(self):
        print("[*]NaverKeywordCrawler Class start...")
        self.keyword = None
        self.keyword_list = []
        self.url_list = []
        self.depth = 0
        self.start_date = None
        self.end_date = None
        self.url_dict = {}
        self.data_dict = {}
        self.url_list_dict = {}
        self.start_date_dict = {}
        self.end_date_dict = {}
        self.compare_date = None
        self.keyword_list_dict = {}
        self.data_list = []
        self.driver = None

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_date(self, start_date, end_date):
        self.start_date = start_date

