import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(data_file):
    with codecs.open(data_file, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    return data

def get_data_from_file(data_file):
    data = get_data(data_file)
    data = [line.strip().split('\t') for line in data]
    return data

def get_data_from_file_with_label(data_file):
    data = get_data(data_file)
    data = [line.strip().split('\t') for line in data]
    data = [line for line in data if len(line) == 2]
    return data

def get_data_from_file_with_label_and_id(data_file):
    data = get_data(data_file)
    data = [line.strip().split('\t') for line in data]
    data = [line for line in data if len(line) == 3]
