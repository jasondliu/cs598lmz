import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(data)

def read_file_lines(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        return f.readlines()

def write_file_lines(filename, data):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.writelines(data)

def read_file_lines_strip(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        return [line.strip() for line in f.readlines()]

def write_file_lines
