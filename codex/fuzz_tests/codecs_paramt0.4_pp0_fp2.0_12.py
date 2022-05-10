import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename, encoding='utf8'):
    with codecs.open(filename, 'r', encoding=encoding, errors='replace_with_space') as f:
        return f.read()

def write_file(filename, content, encoding='utf8'):
    with codecs.open(filename, 'w', encoding=encoding) as f:
        f.write(content)

def read_lines(filename, encoding='utf8'):
    with codecs.open(filename, 'r', encoding=encoding, errors='replace_with_space') as f:
        return f.readlines()

def write_lines(filename, lines, encoding='utf8'):
    with codecs.open(filename, 'w', encoding=encoding) as f:
        f.writelines(lines)

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, obj):
    with open(
