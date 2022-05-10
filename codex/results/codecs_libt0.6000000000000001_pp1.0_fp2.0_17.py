import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

now_time = datetime.now()

def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def get_detail_url(url):
    """获取详情页的所有url"""
    html = get_content(url)
    soup = BeautifulSoup(html, 'lxml')
    a_list = soup.find_all("a", attrs={"class": "content__list--item--aside"})
    for a in a_list:
        detail_url = a['href']
        get_detail(detail_url)

def get
