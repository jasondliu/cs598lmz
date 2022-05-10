import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(path):
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_from_url(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data

def get_data_from_url_with_proxy(url, proxy):
    proxy_support = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    data = response.read()
    return data

def get_data_from_url_with_proxy_and_header(url, proxy, header):
    proxy_support = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxy_support)

