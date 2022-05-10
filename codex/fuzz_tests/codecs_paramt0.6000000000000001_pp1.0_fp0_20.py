import codecs
codecs.register_error("strict", codecs.ignore_errors)

def read_file(file, encoding='utf-8'):
    with codecs.open(file, encoding=encoding, errors="strict") as f:
        return f.read()

def write_file(file, data, encoding='utf-8'):
    with codecs.open(file, "w", encoding=encoding, errors="strict") as f:
        return f.write(data)

def read_file_lines(file, encoding='utf-8'):
    with codecs.open(file, encoding=encoding, errors="strict") as f:
        return f.readlines()

def write_file_lines(file, lines, encoding='utf-8'):
    with codecs.open(file, "w", encoding=encoding, errors="strict") as f:
        return f.writelines(lines)

def load_json(file, encoding='utf-8'):
    return json.loads(read_file(file, encoding))

def dump_json(obj, file
