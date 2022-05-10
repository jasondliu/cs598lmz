import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='replace_with_space') as f:
        return f.read()

def read_data(file_list):
    data = []
    for file in file_list:
        data.append(read_file(file))
    return data

def get_data(file_list):
    data = read_data(file_list)
    return data

def preprocess_data(data):
    data = [d.lower() for d in data]
    data = [d.replace('\n', ' ') for d in data]
    data = [d.replace('\r', ' ') for d in data]
    data = [d.replace('\t', ' ') for d in data]
    data = [d.replace('  ', ' ') for d in data]
    data = [d.replace('  ', ' ') for d in data]
    data =
