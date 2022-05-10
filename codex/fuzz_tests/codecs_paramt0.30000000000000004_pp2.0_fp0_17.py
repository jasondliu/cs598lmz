import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def get_data_with_label(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split('\t'))
    return data

def get_data_with_label_for_dict(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split('\t'))
    return data

def get_data_with_label_for_dict_with_label(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split('\t'))
    return
