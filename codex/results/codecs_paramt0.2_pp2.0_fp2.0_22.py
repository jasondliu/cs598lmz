import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = f.read()
    return data

def get_data_list(file_name):
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = f.readlines()
    return data

def write_data(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8') as f:
        f.write(data)

def write_data_list(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8') as f:
        f.writelines(data)

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
