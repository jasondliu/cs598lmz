import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    data = []
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_data_from_file(filename):
    data = []
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def get_data_from_file_with_label(filename):
    data = []
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def get_data_from_file_with_label_and_id(filename):
    data = []
    with codecs.open(filename, 'r', 'utf
