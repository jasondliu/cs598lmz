import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename, encoding='utf-8', errors='strict'):
    with codecs.open(filename, encoding=encoding, errors=errors) as f:
        return f.read()

def write_file(filename, content, encoding='utf-8', errors='strict'):
    with codecs.open(filename, 'w', encoding=encoding, errors=errors) as f:
        f.write(content)

def read_json(filename, encoding='utf-8', errors='strict'):
    return json.loads(read_file(filename, encoding, errors))

def write_json(filename, content, encoding='utf-8', errors='strict'):
    write_file(filename, json.dumps(content, ensure_ascii=False, indent=2), encoding, errors)

def read_csv(filename, encoding='utf-8', errors='strict'):
    with codecs.open(filename, 'r', encoding=encoding, errors=errors) as f:

