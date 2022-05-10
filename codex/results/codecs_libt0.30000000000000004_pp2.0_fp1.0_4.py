import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#%%

def get_data_from_file(file_name):
    """
    Gets data from file
    """
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def save_data_to_file(file_name, data):
    """
    Saves data to file
    """
    with open(file_name, 'w') as f:
        json.dump(data, f)

def get_data_from_url(url):
    """
    Gets data from url
    """
    response = requests.get(url)
    data = response.json()
    return data

def get_data_from_url_with_params(url, params):
    """
    Gets data from url with parameters
    """
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_data_from
