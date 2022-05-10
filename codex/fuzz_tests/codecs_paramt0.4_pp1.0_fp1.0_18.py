import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
        return f.read()

def get_data_lines(file_name):
    with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
        return f.readlines()

def get_data_lines_with_index(file_name):
    with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
        for i, line in enumerate(f):
            yield i, line

def get_data_lines_with_index_and_strip(file_name):
    with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
        for i, line in enumerate(f):
            yield i, line.strip()

def write_data_lines(file_name, data_lines):
    with codecs.open(
