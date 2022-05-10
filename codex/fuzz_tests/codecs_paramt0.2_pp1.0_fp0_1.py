import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_url(url):
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except urllib2.HTTPError, e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except urllib2.URLError, e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    return None

def get_soup(url):
    html = get_url(url)
    if html:
        return BeautifulSoup(html, 'html.parser')
    return None

def get_soup_from_file(filename):
    with open(filename, 'r') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def get_soup_from_string(string):
    return BeautifulSoup(string, 'html.parser')

def get_soup_from_response(response):
    return BeautifulSoup
