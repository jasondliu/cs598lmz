import codecs
codecs.register_error('surrogate_or_unknown', surrogatepass)

def get_data(filename):
    with open(filename, 'r', encoding='utf-8', errors='surrogate_or_unknown') as f:
        data = f.read()
        return data

def get_lines(filename):
    with open(filename, 'r', encoding='utf-8', errors='surrogate_or_unknown') as f:
        data = f.readlines()
        return data

def get_lines_with_index(filename):
    with open(filename, 'r', encoding='utf-8', errors='surrogate_or_unknown') as f:
        data = f.readlines()
        for i in range(len(data)):
            data[i] = str(i) + '\t' + data[i]
        return data

def write_data(filename, data):
    with open(filename, 'w', encoding='utf-8', errors='surrogate_or_unknown') as f:
        f.write(data)

def write_lines(
