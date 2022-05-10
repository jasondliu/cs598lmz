import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_soup(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return BeautifulSoup(r.text)

def get_all_links(url):
    soup = get_soup(url)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def get_all_links_in_page(url):
    soup = get_soup(url)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def get_all_links_in_page_contain_keyword(url, keyword):
    soup = get_soup(url)
    links = []
    for link in soup.find_all('a'):
        if link.get('href') and keyword in link.get('href'):
            links.append(link.get('href
