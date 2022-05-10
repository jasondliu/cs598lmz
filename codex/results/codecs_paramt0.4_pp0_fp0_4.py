import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def write_data(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def get_data_from_url(url):
    r = requests.get(url)
    return r.content

def write_data_to_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def get_data_from_url_and_write_to_file(url, filename):
    data = get_data_from_url(url)
    write_data_to_file(filename, data)

def get_data_from_url_and_write_to_file_if_not_exists(url, filename):
    if not os.path.exists(filename):
        get_data_from_url_and_write_to_file(url,
