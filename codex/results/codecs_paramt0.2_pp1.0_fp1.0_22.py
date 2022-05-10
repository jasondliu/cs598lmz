import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_from_url(url):
    response = requests.get(url)
    return response.text

def get_data_from_url_with_proxy(url, proxy):
    response = requests.get(url, proxies=proxy)
    return response.text

def get_data_from_url_with_proxy_and_headers(url, proxy, headers):
    response = requests.get(url, proxies=proxy, headers=headers)
    return response.text

def get_data_from_url_with_headers(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def get_data_from_url_with_headers_and_params(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
