import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_lines(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    return data

def get_data_json(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = json.load(f)
    return data

def write_data(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def write_data_json(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        json.dump(data, f)

def write_data_lines
