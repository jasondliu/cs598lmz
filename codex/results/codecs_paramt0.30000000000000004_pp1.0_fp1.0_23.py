import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(path):
    with open(path, 'r', encoding='utf-8', errors='strict') as f:
        data = f.read()
    return data

def get_tag_data(path):
    with open(path, 'r', encoding='utf-8', errors='strict') as f:
        data = f.read()
    return data

def get_tag_data_list(path):
    with open(path, 'r', encoding='utf-8', errors='strict') as f:
        data = f.readlines()
    return data

def get_data_list(path):
    with open(path, 'r', encoding='utf-8', errors='strict') as f:
        data = f.readlines()
    return data

def get_data_list_with_split(path, split):
    with open(path, 'r', encoding='utf-8', errors='strict') as f:
        data = f.readlines()
    return [d
