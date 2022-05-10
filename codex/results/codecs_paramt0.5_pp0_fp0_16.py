import codecs
codecs.register_error('strict', codecs.ignore_errors)


def get_html(url):
    """
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/62.0.3202.75 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    html = html.decode('utf-8', 'strict')
    return html


def get_data(html):
    """
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'lxml')
    data = soup.select('div.list_item')
    for item in data:
        yield {
            'title': item.select('h3.list_item_title')[0
