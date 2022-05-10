import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_info(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h1', id='firstHeading').text
    content = soup.find('div', id='mw-content-text').text
    return title, content

def get_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', href=re.compile('^/wiki/'))
    return links

def get_all_links(url):
    links = get_links(url)
    for link in links:
        if ':' not in link['href']:
            yield link['href']

def get_all_links_recursive(url):
    links = get_links(url)
    for link in links:
        if ':' not in link['href']:
            yield link['href']
        else:
            for
