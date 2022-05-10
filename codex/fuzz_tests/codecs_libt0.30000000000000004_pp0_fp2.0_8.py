import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data(url):
    r = requests.get(url)
    return r.text

def get_urls(html):
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all('a'):
        try:
            urls.append(i['href'])
        except:
            pass
    return urls

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='post-body entry-content')
    for item in items:
        try:
            print(item.text)
        except:
            pass

def main():
    url = 'https://www.blogger.com/profile/01758717222716971264'
    urls = get_urls(get_data(url))
    for url in urls:
        print(
