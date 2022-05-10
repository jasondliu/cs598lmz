import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_data_from_json(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def get_data_from_json_l(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def get_data_from_json_l_with_key(filename, key):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line.strip())[key])
    return data

def get_data_from_json_l_with_key_
