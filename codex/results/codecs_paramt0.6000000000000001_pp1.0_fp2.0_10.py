import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_id(url):
    url = url.split('/')[-1].split('.html')[0]
    return int(url)

def get_detail(url):
    soup = get_soup(url)
    title = soup.find('h3', attrs={'class': 't c-gap-bottom-small'}).get_text()
    p = soup.find('div', attrs={'class': 'line content'})
    p = p.get_text()
    content = p.split('\xa0\xa0\xa0\xa0')[1]
    return title, content

def get_urls():
    urls = []
    for i in range(1, 19):
        for j in range(1, 101):
            url = 'http://www.huxiu.com/channel/{}_{}.html'.format(i, j)
            soup = get_soup(url)
            time.sleep(0.2)
            huxiu = soup
