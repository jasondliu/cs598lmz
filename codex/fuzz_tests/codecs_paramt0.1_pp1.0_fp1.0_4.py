import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_from_url(url):
    response = requests.get(url)
    return response.text

def get_data_from_url_with_proxy(url, proxy):
    response = requests.get(url, proxies=proxy)
    return response.text

def get_data_from_url_with_headers(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def get_data_from_url_with_headers_and_proxy(url, headers, proxy):
    response = requests.get(url, headers=headers, proxies=proxy)
    return response.text

def get_data_from_url_with_headers_and_proxy_and_cookies(url, headers, proxy, cookies):
    response = requests.get
