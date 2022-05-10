import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    data = response.read()
    return data

def get_page(url):
    pattern = re.compile('<span class="current-comment-page">\[(.*?)\]</span>')
    data = get_data(url)
    page = re.findall(pattern, data)
    return page[0]

def get_content(url):
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?
