import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

def get_response(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response

def get_html(response):
    return BeautifulSoup(response.text, 'lxml')

def get_links(html):
    links = []
    for link in html.select('a'):
        href = link.get('href')
        if href.startswith('/wiki/'):
            links.append(href)
    return links

def get_next_link(links):
    for link in links:
        if link.startswith('/wiki/Philosophy'):
            return None
        if link.startswith('/wiki/'):
            return link

def save_links(links):
    with open('links.txt', 'w') as f:
        for link in links:
            f.write(link + '\n')

def load_links():
    with open('links.txt', 'r') as
