from bz2 import BZ2Decompressor
BZ2Decompressor()

# TODO: refactor to use a class

def get_html(url):
    """
    Get the HTML from a URL.
    """
    response = requests.get(url)
    html = response.text
    return html

def get_soup(url):
    """
    Get the BeautifulSoup object from a URL.
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "html5lib")
    return soup

def get_text(url):
    """
    Get the text from a URL.
    """
    html = get_html(url)
    text = html2text(html)
    return text

def get_links(url):
    """
    Get the links from a URL.
    """
    soup = get_soup(url)
    links = soup.find_all("a")
    return links

def get_images(url):
    """
    Get the images from a URL.
    """
    soup = get_soup(url)
    images = soup.find
