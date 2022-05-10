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

def write_data(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def write_data_lines(filename, data):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.writelines(data)

def get_file_list(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_dir_list(path):
    return
