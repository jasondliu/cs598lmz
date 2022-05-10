import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get(url, query):
    if '?' not in url:
        url += '?'
    else:
        url += '&'
    url += urllib.urlencode(query)
    req = urllib2.Request(url)
    return urllib2.urlopen(req)

def get_json(url, query):
    return json.load(get(url, query))

def get_text(url, query, encoding='utf-8'):
    return get(url, query).read().decode(encoding, 'strict')

def get_html(url, query):
    return BeautifulSoup(get_text(url, query), 'xml')

def get_url(url, query):
    return get(url, query).geturl()
