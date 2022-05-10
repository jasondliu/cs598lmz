import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_data_list(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    return data

def write_data(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def write_data_list(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8', 'strict') as f:
        f.writelines(data)

def get_data_list_from_file(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f
