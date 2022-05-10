import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    data = response.read()
    return data

def get_page_num(url):
    data = get_data(url)
    soup = BeautifulSoup(data, 'html.parser')
    page_num = soup.find('div', class_='pagination').find_all('li')[-2].get_text()
    return int(page_num)

def get_image_url(url):
    data = get_data(url)
    soup = BeautifulSoup(data, 'html.parser')
    image_url = soup.find('div', class
