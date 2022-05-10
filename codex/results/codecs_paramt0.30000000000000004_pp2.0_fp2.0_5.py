import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, content):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def read_lines(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def write_lines(filename, lines):
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.writelines(lines)

def read_json(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return json.load(f)

def write_json(filename, content):
    with codecs.open(filename, 'w', 'utf-8', '
