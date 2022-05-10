import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = f.read()
    return data

def get_data_from_url(url):
    response = requests.get(url)
    return response.text

def get_data_from_url_with_headers(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def get_data_from_url_with_auth(url, username, password):
    response = requests.get(url, auth=(username, password))
    return response.text

def get_data_from_url_with_auth_and_headers(url, username, password, headers):
    response = requests.get(url, auth=(username, password), headers=headers)
    return response.text

def get_data_from_url_with_params(url, params):
    response = requests.get(url, params=params)
    return
