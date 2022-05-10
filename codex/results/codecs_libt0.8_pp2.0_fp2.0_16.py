import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
def get_id(url):
    # https://finance.yahoo.com/quote/A?p=A&.tsrc=fin-srch
    return url.split('/')[-1].split('?')[0]


def get_url(id):
    return "https://finance.yahoo.com/quote/%s?p=%s" % (id, id)


def get_data(id):
    url = get_url(id)
    result = requests.get(url)
    content = result.content
    soup = BeautifulSoup(content, "html.parser")
    quote_price_box = soup.find('div', attrs={'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
    quote_price = quote_price_box.find('span').text
    quote_change_box = soup.find('div', attrs={'class': 'D(ib) Va(m
