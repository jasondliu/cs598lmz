import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(filename):
    """
    Returns the text of the file.
    """
    f = codecs.open(filename, 'r', 'utf-8', 'strict')
    text = f.read()
    f.close()
    return text

def get_text_from_url(url):
    """
    Returns the text of the url.
    """
    f = urllib2.urlopen(url)
    text = f.read()
    f.close()
    return text

def get_text_from_html(html):
    """
    Returns the text of the html.
    """
    soup = BeautifulSoup(html)
    text = soup.get_text()
    return text

def get_text_from_html_file(filename):
    """
    Returns the text of the html file.
    """
    html = get_text(filename)
    text = get_text_from_html(html)
    return text

def get_text_from_
