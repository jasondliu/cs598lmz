import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()

def write_file(filename, data):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.write(data)

def read_file_lines(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.readlines()

def write_file_lines(filename, lines):
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        f.writelines(lines)

def read_file_json(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return json.load(f)

def write_file_json(filename, data):
    with codecs.open(filename,
