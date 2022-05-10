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

def get_data_csv(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = csv.reader(f)
    return data

def get_data_json(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = json.load(f)
    return data

def get_data_pickle(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        data = pickle.load(f)
    return data


