import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_data_lines(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def get_data_json(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        return json.load(f)

def write_data(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8', 'strict') as f:
        f.write(data)

def write_data_lines(file_name, data):
    with codecs.open(file_name, 'w', 'utf-8', 'strict') as f:
        f.writelines(data)

def write
