import codecs
codecs.register_error('strict', codecs.ignore_errors)
class HtmlParser(object):
    def __init__(self):
        import requests
        self.url = 'https://news.qq.com/articleList/rolls/'
        self.request = requests.get(self.url)
        self.request.encoding = self.request.apparent_encoding
        self.request.encoding = 'utf-8'
        # print(self.request.text)
        self.data = self.request.text

    def parse(self):
        import json
        import re
        import os
        import datetime
        pattern = re.compile(r'_Callback\((.*)\)$')
        result = pattern.search(self.data)
        if result:
            data = result.group(1)
            js = json.loads(data)
            news = js['article_info']
            for key in news.keys():
                # print(key)
                news_list = news[key]
                # print(news_list)
                for item in news_list
