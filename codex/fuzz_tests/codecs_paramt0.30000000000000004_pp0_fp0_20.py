import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='strict') as f:
        data = json.load(f)
    return data

def get_data_list(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='strict') as f:
        data = json.load(f)
    return data

def get_data_dict(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='strict') as f:
        data = json.load(f)
    return data

def save_data(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_data_list(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8
