import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data

def get_soup(url):
    data = get_data(url)
    soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)
    return soup

def get_links(url):
    soup = get_soup(url)
    links = soup.findAll('a')
    return links

def get_text(url):
    soup = get_soup(url)
    text = soup.getText()
    return text

def get_text_from_links(links):
    text = ""
    for link in links:
        url = link['href']
        text += get_text(url)
    return text

def get_text_from_url(url):
    text = ""
    links = get_links(url)
    text += get_text_from_links(links)
    return text

