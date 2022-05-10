import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = f.read()
    return data

def get_data_lines(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = f.readlines()
    return data

def get_data_json(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = json.load(f)
    return data

def write_data(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(data)

def write_data_lines(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.writelines(data)

def write_data_json
