import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(path):
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(path, content):
    with codecs.open(path, 'w', 'utf-8', 'strict') as f:
        f.write(content)

def read_json(path):
    return json.loads(read_file(path))

def write_json(path, content):
    write_file(path, json.dumps(content, indent=2, sort_keys=True))

def get_file_paths(dir_path, file_ext=None):
    file_paths = []
    for root, _, files in os.walk(dir_path):
        for file_name in files:
            if file_ext is None or file_name.endswith(file_ext):
                file_paths.append(os.path.join(root, file_name))
    return file_path
