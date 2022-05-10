import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(path, encoding='utf8'):
    with codecs.open(path, 'r', encoding=encoding, errors='strict') as f:
        return f.read()

def write_file(path, content, encoding='utf8'):
    with codecs.open(path, 'w', encoding=encoding, errors='strict') as f:
        f.write(content)
