import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_json(url):
    try:
        response = urllib2.urlopen(url)
        json_data = json.load(response)
        return json_data
    except urllib2.URLError, e:
        print 'Error:', e
        return None

def get_json_data(url):
    json_data = get_json(url)
    if json_data is None:
        return None
    else:
        return json_data['data']

def get_json_dataset(url):
    json_data = get_json(url)
    if json_data is None:
        return None
    else:
        return json_data['dataset']

def get_json_dataset_data(url):
    json_data = get_json(url)
    if json_data is None:
        return None
    else:
        return json_data['dataset']['data']

def get_json_dataset_data
