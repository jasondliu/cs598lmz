import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'replace_with_space') as f:
        return f.read()

def write_file(file_path, content):
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(content)

def read_lines(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'replace_with_space') as f:
        return f.readlines()

def write_lines(file_path, content):
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.writelines(content)

def read_json(file_path):
    with codecs.open(file_path, 'r', 'utf-8', 'replace_with_space') as f:
        return json.load(f)

def write
