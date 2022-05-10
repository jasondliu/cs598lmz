import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_data_from_file(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_data_from_file_with_label(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def get_data_from_file_with_label_and_id(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

