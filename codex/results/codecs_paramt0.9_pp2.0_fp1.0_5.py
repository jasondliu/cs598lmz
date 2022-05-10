import codecs
codecs.register_error('ignore', lambda e: ' ')


def _clean(text):
    text = re.sub('<.*?>', ' ', text)
    text = re.sub('&#.*?;', ' ', text)
    text = re.sub('<.*?>', ' ', text)
    text = re.sub('\n', ' ', text).lower()
    return text


def _fetch(url, encoding='utf-8'):
    """
    Fetch a URL and return its content with a gwened encoding,
    or None if an error happened.
    """
    try:
        sock = urlopen(url)
        content = sock.read()
        sock.close()
        content = content.decode(encoding)
    except:
        content = None

    return content


def _parse_page(url, content):
    """
    Parse a page and return the list of news.
    """
    
    class _List(list):
        """
        A simple list that allows to store data in
        its elements attributes.
        """
       
