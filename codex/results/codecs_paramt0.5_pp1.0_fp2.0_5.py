import codecs
codecs.register_error("strict", codecs.ignore_errors)

def get_data(fname):
    with open(fname) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data

def get_data_from_url(url):
    response = requests.get(url)
    return response.text.splitlines()

def get_data_from_url_with_decode(url):
    response = requests.get(url)
    return response.text.splitlines()

def get_data_from_url_with_decode(url):
    response = requests.get(url)
    return response.text.splitlines()

def get_data_from_url_with_decode(url):
    response = requests.get(url)
    return response.text.splitlines()

def get_data_from_url_with_decode(url):
    response = requests.get(url)
    return response.text.splitlines()

def get_data_from_url_with
