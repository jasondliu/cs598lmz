import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# 定义抓取的网址
url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'

# 定义headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 定义获取网页的函数
def get_url(url):
    response = requests.get(url, headers=headers)
    return response.text

# 获取网页源代码
html = get_url(url)

# 定义解析网页的函数
def
