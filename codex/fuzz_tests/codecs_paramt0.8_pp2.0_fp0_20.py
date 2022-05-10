import codecs
codecs.register_error('strict', codecs.ignore_errors)

# init logging
logging.basicConfig()
LOG = logging.getLogger("watto-cleaner")
LOG.setLevel(logging.DEBUG)


def get_name_from_url(url):
    """
    Return the file name in the given url

    >>> get_name_from_url("http://example.com/foo.pdf")
    'foo'
    """
    m = re.match(r'^https?://.*/(.*)$', url)
    if m is None:
        return None
    path = m.group(1)
    return os.path.splitext(path)[0]


def get_host(url):
    """
    Return the host of the url

    >>> get_host("https://example.com/foo.pdf")
    'example.com'
    """
    m = re.match(r'^https?://([^/]*)/.*$', url)
    if m is None:
        return None
    return m.group(1)



