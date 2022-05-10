import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#定义一个类，用来保存一个网页的源码
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        #模拟浏览器
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        headers = {'User-Agent': user_agent}
        #模拟登陆
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        request = urllib.
