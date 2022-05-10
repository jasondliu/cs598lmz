import codecs
codecs.register_error('replace_mixed', codecs.replace_errors)


def get_page(url, retries=3):
    """
    Download a page and return its content.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
    }
    try:
        req = Request(url, headers=headers)
        html = urlopen(req).read()
    except HTTPError as e:
        print('Download error:', e.reason)
        html = None
        if retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return get_page(url, retries - 1)
    return html


def get_all_links(html):
    """
    Return a list of links from html.
    """
    # a regular expression to extract all links from
